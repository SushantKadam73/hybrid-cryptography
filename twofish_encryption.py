from Cryptodome.Cipher import Twofish
from Cryptodome.Util.Padding import pad, unpad

# Function to read the Twofish key from a file
def read_twofish_key(file_path):
    with open(file_path, 'rb') as file:
        key = file.read()
    return key

# Function to perform Twofish encryption
def twofish_encrypt(data, key):
    cipher = Twofish.new(key, Twofish.MODE_ECB)
    ciphertext = cipher.encrypt(pad(data, 16))
    return ciphertext

# File path for the Twofish key
key_file_path = 'keys/twofish_key.bin'

# Read the Twofish key from the file
twofish_key = read_twofish_key(key_file_path)

# Get the input data from the file
input_file_path = 'part2.txt'

with open(input_file_path, 'r') as input_file:
    part1 = input_file.read().strip()

# Convert the input data to bytes
data_bytes = part1.encode('utf-8')

# Encrypt the data using Twofish
encrypted_data = twofish_encrypt(data_bytes, twofish_key)

# Save the encrypted data to a file
output_file_path = 'twofish_ciphertext'
with open(output_file_path, 'wb') as output_file:
    output_file.write(encrypted_data)

print(f"Twofish encryption complete. Ciphertext saved to '{output_file_path}'.")



#or

from twofish import Twofish

# Function to read the Twofish key from a file
def read_twofish_key(file_path):
    with open(file_path, 'rb') as file:
        key = file.read()
    return key

# Function to perform Twofish encryption
def twofish_encrypt(data, key):
    cipher = Twofish(key)
    ciphertext = cipher.encrypt(data)
    return ciphertext

# File path for the Twofish key
key_file_path = 'keys/twofish_key.bin'

# Read the Twofish key from the file
twofish_key = read_twofish_key(key_file_path)

# Get the input data from the file
input_file_path = 'part2.txt'

with open(input_file_path, 'r') as input_file:
    part1 = input_file.read().strip()

# Convert the input data to bytes
# Twofish requires the data to be exactly 16 bytes
data_bytes = part1.encode('utf-8')
assert len(data_bytes) == 16, "Data must be exactly 16 bytes"

# Encrypt the data using Twofish
encrypted_data = twofish_encrypt(data_bytes, twofish_key)

# Save the encrypted data to a file
output_file_path = 'twofish_ciphertext'
with open(output_file_path, 'wb') as output_file:
    output_file.write(encrypted_data)

print(f"Twofish encryption complete. Ciphertext saved to '{output_file_path}'.")