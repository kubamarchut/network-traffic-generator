import sys
import time
import random
import threading

from modules.ftp_gen import *
from modules.http_gen import *
from modules.icmp_gen import *
from modules.telnet_gen import *
from modules.ip_information import *

generate_traffic_functions = [
    {"func": generate_ftp_traffic, "label": "generating ftp traffic"}, 
    {"func": generate_http_traffic, "label": "generating http traffic"}, 
    {"func": generate_icmp_traffic, "label": "generating icmp traffic"}, 
    {"func": generate_telnet_traffic, "label": "generating telnet traffic"}
]

def main_part(thread_time_span, dstIP):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= thread_time_span:  # Check if n seconds have elapsed
            break

        random_function = random.choice(generate_traffic_functions)
        print(random_function["label"])
        random_function["func"](dstIP)
        time.sleep(0.1)

def run_traffic_simultaneously(threads_count, thread_time_span, dstIP, test_dst):
    print("Starting network traffic generator")
    print("destination IP:", dstIP)

    if test_dst:
        ip_information_received = ip_information(dstIP)
        if not ip_information_received:
            print("Traffic destination unreacheble")
            sys.exit()

    print(f"\nstarting {threads_count} threads")
    print(f"each thread will run for {thread_time_span}s\n")

    time.sleep(1)

    threads = []

    for i in range(threads_count):
        thread = threading.Thread(
            target=main_part,
            args=(thread_time_span, dstIP)
        )
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    dstIP = "192.168.0.105"
    threads_count = 1
    thread_time_span = 1
    run_traffic_simultaneously(
        threads_count, 
        thread_time_span, 
        dstIP,
        True
    )