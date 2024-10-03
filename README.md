# Image Writer Script

This script writes an image file to a specified device (e.g., a USB drive) and optionally creates persistent storage on that device. It is useful for creating bootable USB drives with persistent storage, similar to tools like UNetbootin.

## Features

- **Image Writing**: Uses the `dd` command to write an image file to a specified device.
- **Persistent Storage**: Optionally creates a persistent storage file on the device.
- **Error Handling**: Logs errors encountered during the process.
- **User Interaction**: Prompts the user for necessary inputs and confirms actions before proceeding.

## Requirements

- Python 3.x
- `termcolor` module
- `sudo` privileges

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed.
3. Install the required module:
    ```sh
    pip install termcolor
    ```

## Usage

1. Run the script:
    ```sh
    ./image_writer.py
    ```
2. Follow the prompts to:
    - Select the device to write to (e.g., `sda`, `sdb`, `sdc`).
    - Specify the block size (e.g., `1M`, `2M`, `4M`, `8M`).
    - Provide the location of the image file (e.g., `/home/username/Downloads/ubuntu.img`).
    - Choose whether to create persistent storage.
    - Confirm the command before execution.

## Example

```sh
$ ./image_writer.py
```

### Example Output

1. **Listing Block Devices**:
    ```
    NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
    sda           8:0    0 931.5G  0 disk 
    ├─sda1        8:1    0   512M  0 part /boot/efi
    ├─sda2        8:2    0 930.5G  0 part /
    sdb           8:16   1  14.9G  0 disk 
    └─sdb1        8:17   1  14.9G  0 part /media/usb
    ```

2. **User Inputs**:
    ```
    Which device (e.g. sda, sdb, sdc) would you like to write to? sdb
    Block size to use (e.g. 1M, 2M, 4M, 8M, etc.): 4M
    Image location including name (e.g. /home/username/Downloads/ubuntu.img): /home/user/Downloads/ubuntu.img
    Do you want to create persistent storage? (y/n): y
    Enter the size of persistent storage in MB (e.g. 1024 for 1GB): 1024
    ```

3. **Confirmation Prompt**:
    ```
    Would you like to proceed (y/n)? 
    sudo dd if=/home/user/Downloads/ubuntu.img of=/dev/sdb bs=4M && sync 
    ```

4. **Script Execution**:
    ```
    Beginning script...
    ```

5. **Image Writing**:
    ```
    1024+0 records in
    1024+0 records out
    4294967296 bytes (4.3 GB, 4.0 GiB) copied, 120.123 s, 35.8 MB/s
    ```

6. **Persistent Storage Creation**:
    ```
    1024+0 records in
    1024+0 records out
    1073741824 bytes (1.1 GB, 1.0 GiB) copied, 10.123 s, 106 MB/s
    mke2fs 1.45.6 (20-Mar-2020)
    Discarding device blocks: done                            
    Creating filesystem with 262144 4k blocks and 65536 inodes
    Filesystem UUID: 12345678-1234-1234-1234-123456789abc
    Superblock backups stored on blocks: 
            32768, 98304, 163840, 229376

    Allocating group tables: done                            
    Writing inode tables: done                            
    Creating journal (8192 blocks): done
    Writing superblocks and filesystem accounting information: done
    ```

7. **Completion Messages**:
    ```
    IMG has been successfully written to /dev/sdb and finished in 130.45 seconds
    Persistent storage of 1024MB created successfully.
    ```

8. **Error Handling (if any)**:
    ```
    Error creating persistent storage: Command '['sudo', 'dd', 'if=/dev/zero', 'of=/mnt/sdb/casper-rw', 'bs=1M', 'count=1024']' returned non-zero exit status 1.
    ```

## License

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

## Author

Adrian Sanabria-Diaz

Source: Conversation with Copilot, 10/2/2024
(1) github.com. https://github.com/wms910/Trap/tree/fbaa517e161580871f20f005aeeaa1ce90601e66/tools%2Fericw-tools%2Fbin%2FREADME.md.
(2) github.com. https://github.com/duanshuai007/s3c2440/tree/a1937c23f36ff5d92a10cdb8982d5416b7a1a0fb/kernel%2Fdrivers%2Fstaging%2Fcomedi%2Fdrivers%2Faddi-data%2FAPCI1710_Dig_io.c.
