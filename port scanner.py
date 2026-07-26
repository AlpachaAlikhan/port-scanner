import socket
import ipaddress

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    


def main():
    pass

def get_ip():
    ip = input("Enter the IP address to scan: ")
    if ip.count('.') != 3:
        print("Invalid IP address format. Please enter a valid IPv4 address.")
        return get_ip()
    elif not all(0 <= int(part) < 256 for part in ip.split('.')):
        print("Invalid IP address. Each octet must be between 0 and 255.")
        return get_ip()
    return ip

def get_portrange():
    port_range = input("Enter the port range to scan (e.g., 20-80): ")
    try:
        start_port, end_port = map(int, port_range.split('-'))
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        print("Invalid port range. Please enter a valid range (e.g., 20-80).")
        return get_portrange()
    return start_port, end_port

def scan_ports(ip, port_range):
    pass

def print_results(results):
    pass
