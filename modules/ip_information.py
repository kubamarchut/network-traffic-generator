from scapy.all import IP, ICMP, sr1, ARP, Ether, srp
import socket

def reverse_dns(ip_address):
    try:
        domain = socket.gethostbyaddr(ip_address)[0]
        return domain
    except Exception as e:
        return False

def arp_scan(target_ip):
    try:
        # Tworzenie ramki Ethernet (Ether) i zapytania ARP
        arp = ARP(pdst=target_ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")

        # Połączenie ramki Ether z zapytaniem ARP
        packet = ether / arp

        # Wysłanie zapytania ARP i odbiór odpowiedzi
        result = srp(packet, timeout=1, verbose=0)[0]

        # Wyświetlenie uzyskanych odpowiedzi
        for sent, received in result:
            return received[ARP].hwsrc + " " + searchByVendor(received[ARP].hwsrc)
    except Exception as e:
        print(f"Error during ARP scan: {e}")
        return "Unknown"

def ip_information(target_ip):
    print("Verifying reachibility to:", target_ip)
    try:
        #if not arp_scan(target_ip):
        #    print("ARP scan failed")
        #    return False
        # Creating ICMP packet
        packet = IP(dst=target_ip) / ICMP()

        # Sending ICMP packet and receiving response
        response = sr1(packet, timeout=0.5, verbose=0)

        if response:
            print("✔ device with given IP is reachible")
            if response.haslayer("Ether"):  # Sprawdzenie, czy pakiet zawiera warstwę Ether (MAC)
                print("MAC Address:", response.srcmac, searchByVendor(response.srcmac))  # Adres MAC
            else:
                print("MAC Address:", arp_scan(target_ip))

            print("TTL:", response.ttl)  # Time to Live

            if reverse_dns(target_ip):
                print("Reverse DNS:", reverse_dns(target_ip))

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
    from mac_vendor_finder import searchByVendor
    ip_information("192.168.0.105")

else:
    from modules.mac_vendor_finder import searchByVendor
