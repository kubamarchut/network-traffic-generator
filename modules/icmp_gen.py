from scapy.all import IP, ICMP, send

verbose = False

def vprint(str):
    if verbose: print(str)

def generate_icmp_traffic(dstIP):
    try:
        # Creating ICMP packet (ping)
        packet = IP(dst=dstIP) / ICMP()

        # Sending packet
        send(packet, verbose = 0)
        vprint("ICMP Packet Sent")
    except Exception as e:
        vprint("An error occurred:", e)
        
if __name__ == "__main__":
    verbose = True
    #Calling function generating ICMP (ping)
    generate_icmp_traffic("8.8.8.8")  # Ping to Google's DNS server (8.8.8.8)
