from scapy.all import sniff, IP, TCP, UDP, ICMP
from scapy.layers.http import HTTPRequest  # import HTTP packet

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Determine the protocol
        if protocol == 6:
            proto = "TCP"
        elif protocol == 17:
            proto = "UDP"
        elif protocol == 1:
            proto = "ICMP"
        else:
            proto = "Other"

        # Print packet details
        print(f"IP Source: {ip_src}")
        print(f"IP Destination: {ip_dst}")
        print(f"Protocol: {proto}")

        # If the packet has a TCP layer
        if TCP in packet:
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        # If the packet has a UDP layer
        if UDP in packet:
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        # If the packet has an HTTP layer
        if packet.haslayer(HTTPRequest):
            print(f"HTTP Method: {packet[HTTPRequest].Method.decode()}")
            print(f"HTTP Host: {packet[HTTPRequest].Host.decode()}")
            print(f"HTTP Path: {packet[HTTPRequest].Path.decode()}")

        print(f"Payload: {packet[IP].payload}")
        print("="*50)

def main():
    # Start sniffing
    print("Starting packet capture...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
