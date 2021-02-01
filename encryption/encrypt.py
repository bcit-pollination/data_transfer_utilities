from cryptography.fernet import Fernet
from common import load_key

file = "test.key"

key = load_key(file)

msg = "message to encrypt".encode()

f = Fernet(key)

encrypted_msg = f.encrypt(msg)

print(encrypted_msg)