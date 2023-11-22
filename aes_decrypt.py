# decryption_code.py
from Crypto.Cipher import AES
from Crypto.Util.Padding import  unpad  
from Crypto.Random import get_random_bytes


# Function to read the AES key from a file
def read_aes_key(file_path):
    with open(file_path, 'rb') as file:
        key = file.read()
    return key


def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data.decode('utf-8')

# File path for the AES key
key_file_path = 'keys/aes_key.bin'

# Read the AES key from the file
aes_key = read_aes_key(key_file_path)

# Read the encrypted data from the file (replace with the actual file path)
input_file_path = 'aes_ciphertext'
with open(input_file_path, 'rb') as input_file:
    encrypted_data = input_file.read()

# Decrypt the data using AES
decrypted_data = aes_decrypt(encrypted_data, aes_key)

# Print or use the decrypted data as needed
print(f"Decrypted data: {decrypted_data}")
