from scapy.all import *

def generate_icmp_traffic(dstIP):
    try:
        # Creating ICMP packet (ping)
        packet = IP(dst=dstIP) / ICMP()

        # Sending packet
        send(packet, verbose = 0)
        print("ICMP Packet Sent")
    except Exception as e:
        print("An error occurred:", e)
        
if __name__ == "__main__":
    #Calling function generating ICMP (ping)
    generate_icmp_traffic("8.8.8.8")  # Ping to Google's DNS server (8.8.8.8)
