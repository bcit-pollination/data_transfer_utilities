from cryptography.fernet import Fernet
import os
def load_key(key_file):
    return open(key_file, "rb").read()

def generate_key():
    key = Fernet.generate_key()
    with open("./test.key", "wb") as key_file:
        key_file.write(key)


def encrypt_data(filename):

    with open(filename, 'r') as file:
        data = file.read()

    print(data);
    msg = data.encode()
    keyfile = "testing.key"
    key = load_key(keyfile)
    f = Fernet(key)

    encrypted_msg = f.encrypt(msg)

    encrypt_output_file = open("encrypt_output.txt", "wb")
    encrypt_output_file.write(encrypted_msg)
    encrypt_output_file.close()
    os.system('./encode-crc32 encrypt_output.txt > encoded_data.txt')


encrypt_data("test.json")