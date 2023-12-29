import argparse

from main import run_traffic_simultaneously

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Traffic Generator")
    parser.add_argument("--ip", help="Destination IP address", required=True)
    parser.add_argument("--threads", type=int, default=1, help="Number of threads")
    parser.add_argument("--timespan", type=int, default=1, help="Thread time span in seconds")
    parser.add_argument("--test", action="store_true", help="Test destination reachability")

    args = parser.parse_args()

    dstIP = args.ip
    threads_count = args.threads
    thread_time_span = args.timespan

    run_traffic_simultaneously(threads_count, thread_time_span, dstIP, args.test)