import re

class DataFilter:
    def __init__(self, file_path):
        self.file_path = file_path

    def filter_data(self):
        filtered_lines = []
        verification_ip_port = re.compile(
            r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-0]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|['
            r'01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):([0-9]|[1-9][0-9]{1,4})$')
        verification_mac_address = re.compile(r'^([0-9A-Fa-f]{1,2}:){5}[0-9A-Fa-f]{1,2}$')
        verification_udp = re.compile(r'^(true|false)$')
        verification_byte = re.compile(r'^[1-9][0-9]*$')
        verification_transmission_time = re.compile(r'^[0-9]+(\.[0-9]{1,4})?$')

        with open(self.file_path, 'r') as file:
            for line in file:
                elements = line.strip().split(';')
                if (len(elements) == 7 and
                        verification_ip_port.match(elements[0]) and
                        verification_mac_address.match(elements[1]) and
                        verification_ip_port.match(elements[2]) and
                        verification_mac_address.match(elements[3]) and
                        verification_udp.match(elements[4]) and
                        verification_byte.match(elements[5]) and
                        verification_transmission_time.match(elements[6])):
                    filtered_lines.append(elements)

        return filtered_lines
