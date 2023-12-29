import time
import random
import threading

from modules.ftp_gen import *
from modules.http_gen import *
from modules.icmp_gen import *
from modules.telnet_gen import *

dstIP = "192.168.0.105"

generate_traffic_functions = [generate_ftp_traffic, generate_http_traffic, generate_icmp_traffic, generate_telnet_traffic]
def main_part():
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 10:  # Check if 10 seconds have elapsed
            break
        random_function = random.randrange(0, len(generate_traffic_functions))
        print(generate_traffic_functions[random_function].__name__)
        generate_traffic_functions[random_function](dstIP)
        time.sleep(0.1)

threads = []

for i in range(50):
    thread = threading.Thread(target=main_part)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()