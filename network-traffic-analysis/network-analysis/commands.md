# 🧾 Commands Used

## Setup & Installation

sudo apt update && sudo apt upgrade -y

sudo apt install wireshark tcpdump snort -y

sudo usermod -aG wireshark $USER

newgrp wireshark

## Capture Traffic

ip a

tcpdump -D

sudo tcpdump -i eth0 -w capture.pcap

sudo tcpdump -i eth0 -w http_traffic.pcap port 80

sudo tcpdump -i eth0 -c 100 -w sample.pcap

tcpdump -r capture.pcap

## Wireshark

wireshark &

wireshark capture.pcap

Filters:
http
ip.addr == 192.168.1.1
tcp.flags.syn == 1
dns

## Snort

snort -V
sudo snort -i eth0 -v
sudo snort -i eth0 -l /var/log/snort/
sudo snort -i eth0 -c /etc/snort/snort.conf -A console

Custom Rule:
alert icmp any any -> any any (msg:"ICMP Ping Detected"; sid:1000001; rev:1;)
