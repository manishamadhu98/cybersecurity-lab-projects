# 🧾 Commands Used

## Install Tools

sudo apt install hashcat john python3 -y
hashcat --version
john --version

## John the Ripper

gunzip /usr/share/wordlists/rockyou.txt.gz
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
john --show --format=raw-md5 hash.txt
john --format=raw-md5 --incremental hash.txt

## Hashcat

hashcat --example-hashes | grep -i md5
hashcat -m 0 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
hashcat -m 0 -a 3 hash.txt ?l?l?l?l?l?l
hashcat -m 0 hash.txt --show
hashcat -m 1400 -a 0 sha256hash.txt /usr/share/wordlists/rockyou.txt
