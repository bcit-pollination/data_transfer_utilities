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
parser = argparse.ArgumentParser(description='''mode is an integer,
 1:usb \n                                                                    
 2:specific path \n                       
 3:local folder\n''')

# exporting to an usb?              1
#           to a specific path?     2
#           to local folder?        3
parser.add_argument(
'mode',
type=int,
help='''mode is an integer,
 1: usb, will return a list of usb devices and prompts for futher inputs. \n                                                                    
 2: specific path, followed by -d <path> or --dir <path>                      
 3: local folder\n''')

parser.add_argument('-d', '--dir')

args = parser.parse_args()

print(args)

# to usb
if(args.mode == 1):
    mount_points = get_mount_points()
    print(mount_points)
    usb_choice = input("input the index of the usb array(starting from 0):")
    dir = mount_points[int(usb_choice)][1] + "/"


# to a path
elif(args.mode ==2):
    #grabs the --dir argument.
    dir = args.dir
    #error checking for not having a path at all.
    if(dir == None):
        print('''Failed to export,
reason:  You have to specify a path to export using mode 2 !!!''')
    else:
        print('file exporting to "' + dir + '" ...')
# local folder
else: 
    dir = './'

decrypt("testing.key", dir)