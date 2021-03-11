import os


filename = "test.json"
with open(filename, 'r') as fr:
    pre_ = fr.read()
    lines = pre_.split('\n')
    new_filename = filename.split('.')[0]+".txt" # To keep the same name except ext
    with open(new_filename, "a") as fw:
        fw.write("\n".join(lines))


# #encode
# os.system('./encode-crc32 test.json > encoded.txt')

# #decode
# os.system('./decode-crc32 encoded.txt > decoded.json')

#encode
os.system('./encode-crc32 encrypt_output.txt > encoded2.txt')

#decode
os.system('./decode-crc32 encoded2.txt > decoded2.txt')