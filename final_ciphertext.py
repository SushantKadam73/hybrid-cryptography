def combine_files(file_paths, output_file_path, delimiter=b'\0'*16):
    with open(output_file_path, 'wb') as output_file:
        for file_path in file_paths:
            with open(file_path, 'rb') as input_file:
                output_file.write(input_file.read())
                output_file.write(delimiter)

def separate_files(input_file_path, output_file_paths, delimiter=b'\0'*16):
    with open(input_file_path, 'rb') as input_file:
        contents = input_file.read()

    parts = contents.split(delimiter)

    for output_file_path, part in zip(output_file_paths, parts):
        with open(output_file_path, 'wb') as output_file:
            output_file.write(part)

if __name__ == "__main__":
    # Combine the files
    file_paths = ['aes_ciphertext', 'twofish_ciphertext', 'digital_signature.bin']
    output_file_path = 'cipher'
    combine_files(file_paths, output_file_path)

    # Separate the files
    input_file_path = 'cipher'
    output_file_paths = ['aes_ciphertext_out', 'twofish_ciphertext_out', 'digital_signature_out.bin']
    separate_files(input_file_path, output_file_paths)