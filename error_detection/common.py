import os
from cryptography.fernet import Fernet
from glob import glob
from subprocess import check_output, CalledProcessError

def load_key(key_file):
    return open(key_file, "rb").read()

def generate_key():
    key = Fernet.generate_key()
    with open("./test.key", "wb") as key_file:
        key_file.write(key)

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
