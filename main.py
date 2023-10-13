from filter_data import DataFilter
from database import DatabaseManager
from queries import NetworkQueries

# Фильтрация данных
data_filter = DataFilter('traf.txt')
suitable_lines = data_filter.filter_data()

# Работа с базой данных
db_manager = DatabaseManager('filtered_lines_database.db')
db_manager.create_filtered_lines_table()
db_manager.insert_data_into_filtered_lines_table(suitable_lines)

# Выполнение запросов и вывод результатов
network_queries = NetworkQueries('filtered_lines_database.db')

unique_nodes_count = network_queries.get_unique_nodes()
average_network_speed = network_queries.get_average_speed()
udp_speed_comparison = network_queries.get_udp_speed_comparison()
top_10_nodes_by_speed = network_queries.get_top_10_nodes_by_speed()
top_10_subnets_by_sessions = network_queries.get_top_10_subnets_by_sessions()
proxy_nodes = network_queries.get_proxy_nodes()

print(unique_nodes_count)
print(average_network_speed)
print(udp_speed_comparison)
print(top_10_nodes_by_speed)
print(top_10_subnets_by_sessions)
print(proxy_nodes)
