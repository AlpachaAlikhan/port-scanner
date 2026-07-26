import socket
import ipaddress

def main():
    ip = get_ip()
    port_range = get_port_range()
    results = []
    for port in range(port_range):
        if scan_port(ip, port):
            results.append(port)
    print_results(results)
    
        
def get_ip():
    while True:
        ip = input("Enter the IP address to scan: ")

        try:
            ipaddress.ip_address(ip)
            return ip
        except ValueError:
            print("Invalid IP address")
        

def get_port_range():
    while True:
        port_range = input("Enter the port range to scan (e.g., 20-80): ")
        try:
            start_port, end_port = map(int, port_range.split('-'))
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                raise ValueError
            return start_port, end_port
            
        except ValueError:
            print("Invalid port range. Please enter a valid range (e.g., 20-80).")

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            return True 
    except socket.error:
        return False


def print_results(results):
    print("========\nOpen ports\n\n")
    for result in results:
        print(results) 
    print(f"Total: {len(results)}\n========")
    

scan_port("1.1.1.1", 44)