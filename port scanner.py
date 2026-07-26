import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


MAX_WORKERS = 100
TIMEOUT = 1

def main():
    ip = get_ip()
    start_port, end_port = get_port_range()
    results = []
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(scan_port, ip, port) : port
            for port in range(start_port, end_port + 1)
        }

        for future in as_completed(futures):
            port = futures[future]
            if future.result():
                results.append(port)
    end = time.perf_counter()

    print_results(sorted(results), end - start)
    
        
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
        sock.settimeout(TIMEOUT)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return True 
        return False
   


def print_results(results, elapsed_time):
    print("========\nOpen ports\n\n")
    for result in results:
        try:
            print(f"{result}   {socket.getservbyport(result)}")
        except OSError:
            print(result) 
    print(f"Total: {len(results)}\nScan completed in {elapsed_time:.2f} seconds.\nThreads: {MAX_WORKERS}\n\n========")
    

main()