from cryptography.fernet import Fernet
import os

def load_key(key_file):
    return open(key_file, "rb").read()

os.system('./decode-crc32 encoded_data.txt > decoded_data.txt')

with open('decoded_data.txt', 'rb') as file:
    data = file.read()


keyfile = "testing.key"
key = load_key(keyfile)
f = Fernet(key)
decrypted_msg = f.decrypt(data)

print(decrypted_msg)
encrypt_output_file = open("data.json", "wb")
encrypt_output_file.write(decrypted_msg)
encrypt_output_file.close()