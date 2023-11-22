#include <cryptopp/twofish.h>
#include <cryptopp/hex.h>
#include <cryptopp/files.h>
#include <fstream>
#include <iostream>

int main() {
    CryptoPP::byte key[CryptoPP::Twofish::DEFAULT_KEYLENGTH], iv[CryptoPP::Twofish::BLOCKSIZE];

    // Read the key from the file
    std::ifstream key_file("keys/twofish_key.bin", std::ios::binary);
    key_file.read(reinterpret_cast<char*>(key), CryptoPP::Twofish::DEFAULT_KEYLENGTH);
    key_file.close();

    memset(iv, 0x00, CryptoPP::Twofish::BLOCKSIZE);

    // Read the input text from the file
    std::ifstream input_file("input2.txt");
    std::string plaintext((std::istreambuf_iterator<char>(input_file)), std::istreambuf_iterator<char>());
    input_file.close();

    std::string ciphertext;
    std::string decryptedtext;

    std::cout << "Plaintext: " << plaintext << std::endl;

    CryptoPP::Twofish::Encryption encryption(key, CryptoPP::Twofish::DEFAULT_KEYLENGTH);
    CryptoPP::CBC_Mode_ExternalCipher::Encryption cbcEncryption(encryption, iv);

    CryptoPP::StreamTransformationFilter stfEncryptor(cbcEncryption, new CryptoPP::StringSink(ciphertext));
    stfEncryptor.Put(reinterpret_cast<const unsigned char*>(plaintext.c_str()), plaintext.length() + 1);
    stfEncryptor.MessageEnd();

    std::cout << "Ciphertext: ";
    CryptoPP::StringSource ss(ciphertext, true, new CryptoPP::HexEncoder(new CryptoPP::FileSink(std::cout)));
    std::cout << std::endl;

    return 0;
}