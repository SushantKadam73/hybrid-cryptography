# encryption_script.py

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad  
from Crypto.Random import get_random_bytes


# Function to read the AES key from a file
def read_aes_key(file_path):
    with open(file_path, 'rb') as file:
        key = file.read()
    return key

# Function to perform AES encryption
def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    return ciphertext

def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data.decode('utf-8')

# File path for the AES key
key_file_path = 'keys/aes_key.bin'

# Read the AES key from the file
aes_key = read_aes_key(key_file_path)

# Get the input data from the file
input_file_path = 'part1.txt'

with open(input_file_path, 'r') as input_file:
    part1 = input_file.read().strip()

# Convert the input data to bytes
data_bytes = part1.encode('utf-8')

# Encrypt the data using AES
encrypted_data = aes_encrypt(data_bytes, aes_key)

# Save the encrypted data to a file
output_file_path = 'aes_ciphertext'
with open(output_file_path, 'wb') as output_file:
    output_file.write(encrypted_data)

print(f"AES encryption complete. Ciphertext saved to '{output_file_path}'.")


# Decrypt the data using AES
decrypted_data = aes_decrypt(encrypted_data, aes_key)

# Save the decrypted data to a file
decrypted_file_path = 'decrypt1.txt'
with open(decrypted_file_path, 'w') as decrypted_file:
    decrypted_file.write(decrypted_data)

print(f"Decrypted data saved to '{decrypted_file_path}'.")
