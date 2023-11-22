from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

def load_private_key(private_key_path):
    with open(private_key_path, 'rt') as f:
        private_key = ECC.import_key(f.read())
    return private_key

def generate_ecdsa_signature(private_key, file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    hash_obj = SHA256.new(data)
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    return signature

# Load the private key
private_key = load_private_key('keys/ecc_private_key.pem')

# Generate the ECDSA signature
digital_signature = generate_ecdsa_signature(private_key, 'text.txt')

# Save the digital signature
def save_signature(signature, file_path):
    with open(file_path, 'wb') as f:
        f.write(signature)

save_signature(digital_signature, 'keys/digital_signature.bin')

print('Digital Signature saved to keys/digital_signature.bin')

print('Digital Signature:', digital_signature)