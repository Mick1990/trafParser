import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_filtered_lines_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS filtered_lines_table (
                obtained_ip TEXT,
                obtained_mac TEXT,
                sent_ip TEXT,
                sent_mac TEXT,
                udp TEXT,
                size INTEGER,
                time REAL
            )
        ''')
        self.conn.commit()

    def insert_data_into_filtered_lines_table(self, data):
        self.cursor.executemany('''
            INSERT INTO filtered_lines_table
            (obtained_ip, obtained_mac, sent_ip, sent_mac, udp, size, time)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', data)
        self.conn.commit()
