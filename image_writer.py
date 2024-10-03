#!/usr/bin/env python3
import time
import subprocess
import os
import logging
from termcolor import colored

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_persistent_storage(device, size):
    """Creates a persistent storage file on the specified device."""
    persistent_file = f"/mnt/{device}/casper-rw"
    try:
        subprocess.run(['sudo', 'mkdir', '-p', f"/mnt/{device}"], check=True)
        subprocess.run(['sudo', 'mount', f"/dev/{device}", f"/mnt/{device}"], check=True)
        subprocess.run(['sudo', 'dd', 'if=/dev/zero', f"of={persistent_file}", f"bs=1M", f"count={size}"], check=True)
        subprocess.run(['sudo', 'mkfs.ext4', '-F', persistent_file], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error creating persistent storage: {e}")
    finally:
        subprocess.run(['sudo', 'umount', f"/mnt/{device}"], check=True)
        logging.info(f"Persistent storage of {size}MB created successfully.")

def image_write():
    """Writes an image to a specified device using the dd command."""
    try:
        print(subprocess.run(['lsblk', '-p'], capture_output=True, text=True).stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error listing block devices: {e}")
        return
    
    device_to_write_to = input('Which device (e.g. sda, sdb, sdc) would you like to write to? ')
    block_size = input('Block size to use (e.g. 1M, 2M, 4M, 8M, etc.): ')
    image_to_write = input('Image location including name (e.g. /home/username/Downloads/ubuntu.img): ')
    persistent_storage = input('Do you want to create persistent storage? (y/n): ')
    
    full_bash_command = f"sudo dd if={image_to_write} of=/dev/{device_to_write_to} bs={block_size} && sync"
    answer = input(colored(f'\n\nWould you like to proceed (y/n)? \n\n{full_bash_command} ', 'blue'))
    
    if answer.lower() in ['y', 'yes']:
        print('Beginning script...')
        start = time.time()
        try:
            subprocess.run(full_bash_command, shell=True, check=True)
            if persistent_storage.lower() in ['y', 'yes']:
                storage_size = input('Enter the size of persistent storage in MB (e.g. 1024 for 1GB): ')
                create_persistent_storage(device_to_write_to, storage_size)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error writing image: {e}")
        else:
            duration = time.time() - start
            logging.info(f'IMG has been successfully written to /dev/{device_to_write_to} and finished in {duration:.2f} seconds')
    else:
        print('Cancelled...')

def main():
    """Main function to execute the image writing process."""
    image_write()

if __name__ == '__main__':
    main()
