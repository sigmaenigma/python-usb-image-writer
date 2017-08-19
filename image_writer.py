#!/usr/bin/env python3
import datetime
import time
import getpass
from subprocess import Popen
import os
from termcolor import colored

# -*- coding: utf-8 -*-
#
# 	image_writer.py
#  
# 	Copyright 2017 Adrian Sanabria-Diaz <sigmacts@gmail.com>
#  
# 	This program is free software; you can redistribute it and/or modify
# 	it under the terms of the GNU General Public License as published by
# 	the Free Software Foundation; either version 2 of the License, or
# 	(at your option) any later version.
#  
# 	This program is distributed in the hope that it will be useful,
# 	but WITHOUT ANY WARRANTY; without even the implied warranty of
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# 	GNU General Public License for more details.
# 
# 	You should have received a copy of the GNU General Public License
# 	along with this program; if not, write to the Free Software
# 	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# 	MA 02110-1301, USA.
#
#	This script writes an img to a Flash drive (e.g. /dev/sdb) using the dd command.
#
#	Use at your own risk


def image_write():
	print(os.system('lsblk -p'))
	device_to_write_to = input('Which device (e.g. sda, sdb, sdc) would you like to write to?')
	block_size = input('Block size to use (e.g. 1M, 2M, 4M, 8M, etc.): ')
	image_to_write = input('Image location including name (e.g. /home/username/Downloads/ubuntu.img): ')

	full_bash_command = "sudo dd if=/dev/" + device_to_write_to + " of=" + image_to_write + ' && sync'
	answer = input(colored('\n\nWould you like to proceed (y/n)? \n\n' + full_bash_command + ' ', 'blue'))
	if answer in ['Y', 'y', 'Yes', 'yes']:
		print('Beginning script...')
		start = time.time()
		try:		
			Popen(full_bash_command, shell=True).wait()
		except Exception as e:
			print(str(e))

		print('IMG has been successfuly written to /dev/' + device_to_write_to +' and finished in '+str(time.time()-start)+' seconds')

	else:
		print('Cancelled...')


def main():
	image_write()

if __name__ == '__main__':
	main()
