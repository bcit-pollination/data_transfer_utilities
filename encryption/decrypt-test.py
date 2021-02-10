from cryptography.fernet import Fernet
from common import load_key
import sys


file = "test.key"

key = load_key(file)

f = Fernet(key)

# First arg should be an encrypted msg example: b'gAAAAABgGET1iqrsmBrqHf9M2qq28zDqaTSa1EHK0FL0HOUGEHC0YFSYolhjmyfHMJAhlJsVcb4CpsjJnni6q8vEGtB20MQEmMzq3wQBN1WmltLY-_yjzUo='
encrypted_msg = sys.argv[1]

decrypted_msg = f.decrypt(encrypted_msg)
print(decrypted_msg.decode())