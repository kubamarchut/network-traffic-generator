import time
import random
import threading

from modules.ftp_gen import *
from modules.http_gen import *
from modules.icmp_gen import *
from modules.telnet_gen import *

generate_traffic_functions = [
    generate_ftp_traffic, 
    generate_http_traffic, 
    generate_icmp_traffic, 
    generate_telnet_traffic
]

def main_part(thread_time_span):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= thread_time_span:  # Check if n seconds have elapsed
            break
        
        random_function = random.choice(generate_traffic_functions)
        print(random_function.__name__)
        random_function(dstIP)
        time.sleep(0.1)

def run_traffic_simultaneously(threads_count, thread_time_span):
    threads = []

    for i in range(threads_count):
        thread = threading.Thread(target=main_part, args=(thread_time_span))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    dstIP = "192.168.0.105"
    threads_count = 50
    thread_time_span = 10
    run_traffic_simultaneously(threads_count, thread_time_span)