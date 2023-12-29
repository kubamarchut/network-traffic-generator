from scapy.all import IP, ICMP, sr1, ARP, Ether, srp
import socket

def arp_scan(target_ip):
    try:
        # Tworzenie ramki Ethernet (Ether) i zapytania ARP
        arp = ARP(pdst=target_ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")

        # Połączenie ramki Ether z zapytaniem ARP
        packet = ether / arp

        # Wysłanie zapytania ARP i odbiór odpowiedzi
        result = srp(packet, timeout=3, verbose=0)[0]

        # Wyświetlenie uzyskanych odpowiedzi
        for sent, received in result:
            return received[ARP].hwsrc
    except Exception as e:
        print(f"Error during ARP scan: {e}")
        return "Unknown"

def ip_information(target_ip):
    try:
        # Creating ICMP packet
        packet = IP(dst=target_ip) / ICMP()

        # Sending ICMP packet and receiving response
        response = sr1(packet, timeout=2, verbose=0)

        if response:
            #print("IP Address:", response.src)
            print("Reverse DNS:", socket.gethostbyaddr(response.src)[0])
            if response.haslayer("Ether"):  # Sprawdzenie, czy pakiet zawiera warstwę Ether (MAC)
                print("MAC Address:", response.srcmac)  # Adres MAC
            else:
                print("MAC Address:", arp_scan(target_ip))

            print("TTL:", response.ttl)  # Time to Live

            # print(response.summary())  # Packet summary
            return True
        else:
            print("No response from the IP:", target_ip)
            return False
    except Exception as e:
        print(f"Error during IP information retrieval: {e}")
        return False

if __name__ == "__main__":
    # Użycie funkcji do uzyskania informacji o danym adresie IP
    ip_information("192.168.0.105")
