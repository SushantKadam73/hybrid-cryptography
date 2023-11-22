import os
import hashlib
from key_gen import key_generation
from Crypto.Cipher import AES

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def divide_text(text):
    total_length = len(text)
    midpoint = total_length // 2

    part1 = text[:midpoint]
    part2 = text[midpoint:]

    return part1, part2

def save_to_file(data, file_path):
    with open(file_path, 'w') as f:
        f.write(data)

if __name__ == "__main__":
    # Generate keys using the function from key_gen.py
    key_generation()

    # Divide text
    file_path = os.path.join("text.txt")
    file_content = read_file(file_path)
    part1, part2 = divide_text(file_content)

    # Save part1 and part2 to separate files
    save_to_file(part1, 'part1.txt')
    save_to_file(part2, 'part2.txt')

    # Display the results
    print("\nDivided Parts:")
    print("Part 1:", part1)
    print("Part 2:", part2)
    
    def get_part1():
        return part1
    
    def get_part2():
        return part2
    
# Generating hash using SHA-256 algorithm 

def generate_file_hash(file_path):
    # Open the file in binary mode and read its contents
    with open(file_path, 'rb') as f:
        data = f.read()

    # Create a new SHA256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the data
    hash_object.update(data)

    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()



    return hash_hex

# Usage
hash_value = generate_file_hash('text.txt')
print('SHA256 hash of the file:', hash_value)

 # Save the hash to a file
with open("hash_value.txt", "w") as hash_file:
    hash_file.write(hash_value)

