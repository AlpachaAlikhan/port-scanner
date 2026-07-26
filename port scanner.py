import socket
import ipaddress
import time


def main():
    ip = get_ip()
    port_range = get_port_range()
    results = []
    start = time.perf_counter()
    for port in (range(port_range[0], port_range[1] + 1)):
        if scan_port(ip, port):
            results.append(port)
    end = time.perf_counter()

    print_results(results, end - start)
    
        
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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return True 
        return False
   


def print_results(results, time):
    global start, end
    print("========\nOpen ports\n\n")
    for result in results:
        try:
            print(result + "   " + socket.getservbyport(result))
        except:
            print(result) 
    print(f"Total: {len(results)}\nScan completed in {time:.2f} seconds.\n\n========")
    

main()