import sqlite3

class NetworkQueries:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def get_unique_nodes(self):
        self.cursor.execute('''
            SELECT COUNT(DISTINCT obtained_ip) + COUNT(DISTINCT sent_ip) AS unique_nodes
            FROM filtered_lines_table
        ''')
        result = self.cursor.fetchone()[0]
        return f'Q1. Уникальных узлов в сети: {result}.'

    def get_average_speed(self):
        self.cursor.execute('''
            SELECT ROUND(AVG(size / time), 2) AS average_speed
            FROM filtered_lines_table
        ''')
        result = self.cursor.fetchone()[0]
        return f'Q2. Средняя скорость передачи данных всей наблюдаемой сети: {result} (байт/сек)'

    def get_udp_speed_comparison(self):
        self.cursor.execute('''
                    SELECT AVG(CASE WHEN udp = 'true' THEN size / time ELSE NULL END) AS udp_speed,
                           AVG(CASE WHEN udp = 'false' THEN size / time ELSE NULL END) AS tcp_speed
                    FROM filtered_lines_table
                ''')
        udp_speed, tcp_speed = self.cursor.fetchone()

        if udp_speed > tcp_speed:
            return f'Q3. Утверждение "UDP используется для передачи данных с максимальной пиковой скоростью" верно.'
        else:
            return f'Q3. Утверждение "UDP используется для передачи данных с максимальной пиковой скоростью" неверно.'

    def get_top_10_nodes_by_speed(self):
        self.cursor.execute('''
            SELECT obtained_ip
            FROM filtered_lines_table
            GROUP BY obtained_ip
            ORDER BY AVG(size / time) DESC
            LIMIT 10
        ''')
        result = self.cursor.fetchall()

        text = f'Q4. 10 узлов сети с самой высокой средней скоростью:\n'

        for item in result:
            text += f'{item[0]}\n'

        return text

    def get_top_10_subnets_by_sessions(self):
        self.cursor.execute('''
                SELECT SUBSTR(obtained_ip, 1, LENGTH(obtained_ip) - 1) AS subnet, COUNT(*) AS session_count
                FROM filtered_lines_table
                GROUP BY subnet
                ORDER BY session_count DESC
                LIMIT 10
            ''')
        result = self.cursor.fetchall()

        text = f'Q5. 10 самых активных подсетей /24 (A.B.C.xxx) по количеству сессий передачи данных:\n'

        for item in result:
            text += f'{item[0]}\n'

        return text

    def get_proxy_nodes(self):
        self.cursor.execute('''
            SELECT proxy_node
            FROM (
              SELECT CASE WHEN COUNT(DISTINCT udp) > 1 THEN obtained_ip ELSE NULL END AS proxy_node
              FROM filtered_lines_table
              GROUP BY obtained_ip, sent_ip
            ) AS subquery
            WHERE proxy_node IS NOT NULL
        ''')
        result = self.cursor.fetchall()

        text = f'Q6. Узлы, которые могут являться посредниками:\n'

        if len(result) == 0:
            text += 'Таких узлов нет'
        else:
            for item in result:
                text += f'{item[0]}\n'

        return text
