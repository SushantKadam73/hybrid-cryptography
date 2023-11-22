from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

def load_public_key(public_key_path):
    with open(public_key_path, 'rt') as f:
        public_key = ECC.import_key(f.read())
    return public_key

def verify_ecdsa_signature(public_key, signature, file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    hash_obj = SHA256.new(data)
    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(hash_obj, signature)
        with open('output.txt', 'w') as f:
            f.write(hash_obj.hexdigest())
    except ValueError:
        print("The signature is not valid.")

# Load the public key
public_key = load_public_key('keys/ecc_public_key.pem')

# Load the signature
with open('keys/digital_signature.bin', 'rb') as f:
    digital_signature = f.read()

# Verify the signature
verify_ecdsa_signature(public_key, digital_signature, 'text.txt')