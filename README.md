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

You will be prompted to enter the device, block size, image location, and whether you want to create persistent storage. The script will then write the image to the specified device and optionally create persistent storage.

## License

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

## Author

Adrian Sanabria-Diaz
