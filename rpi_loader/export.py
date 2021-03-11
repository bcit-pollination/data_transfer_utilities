import os
import sys
from cryptography.fernet import Fernet
from common import load_key
def encrypt_data(filename, keyfile, output_path):

    with open(filename, 'r') as file:
        data = file.read()

    msg = data.encode()

    key = load_key(keyfile)
    f = Fernet(key)

    encrypted_msg = f.encrypt(msg)

    encrypt_output_file = open("tmp.txt", "wb")
    encrypt_output_file.write(encrypted_msg)
    encrypt_output_file.close()
    os.system('./encode-crc32 tmp.txt > {}encoded_data.txt'.format(output_path))


encrypt_data(sys.argv[1], sys.argv[2], sys.argv[3])