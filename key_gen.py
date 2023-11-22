from Crypto.Cipher import AES
from cryptography.hazmat.backends import default_backend  # Import default_backend here
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from Crypto.Random import get_random_bytes
import os

def key_generation():
    return print("Creating Random Keys...")

def generate_aes_key():
    return get_random_bytes(32)  # 256 bits for AES

def generate_twofish_key():
    return get_random_bytes(32)  # 256 bits for Twofish

def generate_ecc_keypair():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def save_key_to_file(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

# Create keys folder if not exists
keys_folder = 'keys'
os.makedirs(keys_folder, exist_ok=True)

# Generate and save AES key
aes_key = generate_aes_key()
aes_key_file_path = os.path.join(keys_folder, 'aes_key.bin')
save_key_to_file(aes_key, aes_key_file_path)

# Generate and save Twofish key
twofish_key = generate_twofish_key()
twofish_key_file_path = os.path.join(keys_folder, 'twofish_key.bin')
save_key_to_file(twofish_key, twofish_key_file_path)

# Generate and save ECC keypair
ecc_private_key, ecc_public_key = generate_ecc_keypair()
ecc_private_key_file_path = os.path.join(keys_folder, 'ecc_private_key.pem')
ecc_public_key_file_path = os.path.join(keys_folder, 'ecc_public_key.pem')

# Save ECC private key
with open(ecc_private_key_file_path, 'wb') as private_key_file:
    private_key_file.write(ecc_private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Save ECC public key
with open(ecc_public_key_file_path, 'wb') as public_key_file:
    public_key_file.write(ecc_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("AES Key saved to:", aes_key_file_path)
print("Twofish Key saved to:", twofish_key_file_path)
print("ECC Private Key saved to:", ecc_private_key_file_path)
print("ECC Public Key saved to:", ecc_public_key_file_path)




