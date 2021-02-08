import os
import argparse
from cryptography.fernet import Fernet
from common import load_key, get_usb_devices, get_mount_points

def decrypt(keyfile, output_path):
    os.system('./decode-crc32 encoded_data.txt > decoded_data.txt')

    with open('decoded_data.txt', 'rb') as file:
        data = file.read()

    key = load_key(keyfile)
    f = Fernet(key)
    decrypted_msg = f.decrypt(data)

    encrypt_output_file = open('{}data.json'.format(output_path), "wb")
    encrypt_output_file.write(decrypted_msg)
    encrypt_output_file.close()

# parsing arguments
parser = argparse.ArgumentParser(description='Program that decodes & decrypts encoded files into data.json')

# Manditory args
parser.add_argument('key', help = 'key file used for encryption')
# Optional args
parser.add_argument('-d', '--dir', help = 'directory path for the encoded output')
parser.add_argument('-u', '--usb', help = 'will provide list of located usbs for selecting encoded output location', action='store_true')

args = parser.parse_args()
print(args)


if(args.usb and (args.dir != None)):
    print("Please choose export location as a directory OR a USB")
    exit()


# to usb
elif(args.usb):
    mount_points = get_mount_points()
    print(mount_points)
    usb_choice = input("input the index of the usb array(starting from 0):")
    dir = mount_points[int(usb_choice)][1] + "/"
    print('file exporting to "' + dir + '" ...')

# to a path
elif(args.dir != None):
    #grabs the --dir argument.
    dir = args.dir
    
    print('file exporting to "' + dir)

# local folder
else: 
    dir = './'
    print('No directory specified file exporting to "' + dir)

decrypt(args.key, dir)