# brute_force_demo.py
import hashlib
import itertools
import string
import time

def brute_force_md5(target_hash, max_length=4):
    chars = string.ascii_lowercase + string.digits
    print(f"[*] Target Hash: {target_hash}")
    print(f"[*] Charset: {chars}")
    attempts = 0
    start = time.time()

    for length in range(1, max_length + 1):
        for combo in itertools.product(chars, repeat=length):
            guess = ''.join(combo)
            hashed = hashlib.md5(guess.encode()).hexdigest()
            attempts += 1
            if hashed == target_hash:
                elapsed = time.time() - start
                print(f"\n[+] CRACKED: '{guess}'")
                print(f"[+] Attempts: {attempts} | Time: {elapsed:.2f}s")
                return guess

    print("[-] Password not found in range.")
    return None

# Generate hash of a short password and crack it
test_pw = "ab12"
test_hash = hashlib.md5(test_pw.encode()).hexdigest()
brute_force_md5(test_hash)
