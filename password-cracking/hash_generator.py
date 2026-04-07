# hash_generator.py
import hashlib, os

password = "MySecret123"

# MD5 (weak - no salt)
md5 = hashlib.md5(password.encode()).hexdigest()

# SHA256 (stronger - no salt)
sha256 = hashlib.sha256(password.encode()).hexdigest()

# SHA256 with Salt (best practice)
salt = os.urandom(16).hex()
salted = hashlib.sha256((salt + password).encode()).hexdigest()

print(f"Password : {password}")
print(f"MD5      : {md5}")
print(f"SHA256   : {sha256}")
print(f"Salt     : {salt}")
print(f"Salted   : {salted}")

# Save MD5 hash to file for cracking
with open("hash.txt", "w") as f:
    f.write(md5)
print("\n[+] MD5 hash saved to hash.txt")
