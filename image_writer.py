#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# 	image_writer.py
#  
# 	Copyright 2016 Adrian Sanabria-Diaz <sigmacts@gmail.com>
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
#	This script basically writes an img to a Flash drive (e.g. /dev/sdb)


import datetime
import time
import getpass
from subprocess import Popen


un = getpass.getuser()	#	Gets the username of the logged in user running this script
fn = 'ubuntu-mate-16.04-desktop-armhf-raspberry-pi.img'	# Filename
img = '/home/'+un+'/Downloads/Torrents/'+fn	# Location of the .img file
dn = '/dev/sdb'	# Device to we're writing to
bs = 'bs=1M'	# Block Size to be written (8 Megabytes default)


def main():
	x = 'sudo dd if='+dn+' of='+img+' '+bs+' '+'&&'+' sync'
	#x = 'sudo apt-get -y update'
	while True:
		script = input('\nDoes the following look correct? (y/n)\n\n'+x+'\n\n')
		if script in ['Y', 'y', 'Yes', 'yes']:
			break
	if script in ['Y', 'y', 'Yes', 'yes']:
		print('Beginning script')
		start = time.time()
		try:		
			Popen(x, shell=True).wait()
		except Exception as e:
			print(str(e))	
		print('IMG has been successfuly written to '+dn+' and finished in '+str(time.time()-start)+' seconds')
	else:
		print('You said no!')


if __name__ == '__main__':
	main()
