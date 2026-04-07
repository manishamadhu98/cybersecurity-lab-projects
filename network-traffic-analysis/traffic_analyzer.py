# traffic_analyzer.py
from scapy.all import rdpcap, IP, TCP, UDP
from collections import Counter

def analyze_pcap(file):
    packets = rdpcap(file)
    src_ips = []
    dst_ports = []

    for pkt in packets:
        if IP in pkt:
            src_ips.append(pkt[IP].src)
        if TCP in pkt:
            dst_ports.append(pkt[TCP].dport)
        elif UDP in pkt:
            dst_ports.append(pkt[UDP].dport)

    print("\n[+] Top 10 Source IPs:")
    for ip, count in Counter(src_ips).most_common(10):
        print(f"    {ip} --> {count} packets")

    print("\n[+] Top 10 Destination Ports:")
    for port, count in Counter(dst_ports).most_common(10):
        print(f"    Port {port} --> {count} hits")

analyze_pcap("capture.pcap")
