import os
from glob import glob
import argparse
from subprocess import check_output, CalledProcessError

def get_usb_devices():
    sdb_devices = map(os.path.realpath, glob('/sys/block/sd*'))
    usb_devices = (dev for dev in sdb_devices
        if 'usb' in dev.split('/')[5])
    # return dict((os.path.basename(dev), dev) for dev in usb_devices)
    ## INTERESTING THOUGH, sdb_devices worked for me, usb_devices didn't
    return dict((os.path.basename(dev), dev) for dev in sdb_devices)

def get_mount_points(devices=None):
    devices = devices or get_usb_devices()  # if devices are None: get_usb_devices
    output = check_output(['mount']).splitlines()
    output = [tmp.decode('UTF-8') for tmp in output]

    def is_usb(path):
        return any(dev in path for dev in devices)
    usb_info = (line for line in output if is_usb(line.split()[0]))
    return [(info.split()[0], info.split()[2]) for info in usb_info]




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
    print(mount_points[usb_choice])


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



## the following formatting works in print, not in --help, which is confusing
#print(('''mode is an integer,
# 1:usb \n                                                                    
# 2:specific path \n                       
# 3:local folder\n'''))


# x = get_mount_points()

# print(x)