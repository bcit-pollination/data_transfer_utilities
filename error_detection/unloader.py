from cryptography.fernet import Fernet
from common import load_key
import os

def decrypt(keyfile)
    os.system('./decode-crc32 encoded_data.txt > decoded_data.txt')

    with open('decoded_data.txt', 'rb') as file:
        data = file.read()

    key = load_key(keyfile)
    f = Fernet(key)
    decrypted_msg = f.decrypt(data)

    encrypt_output_file = open("data.json", "wb")
    encrypt_output_file.write(decrypted_msg)
    encrypt_output_file.close()

decrypt("testing.key")