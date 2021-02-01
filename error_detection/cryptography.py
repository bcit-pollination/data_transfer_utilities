import os

#encryption
os.system('./encode-crc32 test.txt > encoded.txt')

#decryption
os.system('./decode-crc32 encoded.txt > decrypted.txt')