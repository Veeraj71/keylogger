# Keylogger

## Overview

This is a simple Python-based keylogger that records all keystrokes entered on the victim's machine. The captured keystrokes are stored in an encrypted format in a file named `input.py`. The decryption functionality is provided in `decrypt.py`. The project also includes plans to upload the encrypted file to Dropbox (feature under development).

## Features

- Records all keystrokes while the script is running.
- Stops recording when the `ESC` key is pressed.
- Saves keystrokes in an encrypted format to ensure data confidentiality.
- Provides a decryption script to retrieve the recorded keystrokes.
- Upcoming: Automatic upload of encrypted data to Dropbox.

## Prerequisites

- Python 3.x
- Required libraries (install via `pip`):
  - `pynput`
  - `cryptography`
  - `dropbox` (for the upcoming feature)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/keylogger.git
   cd keylogger
   ```
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the keylogger script:
   ```bash
   python keylogger.py
   ```
2. The script will record all keystrokes until the `ESC` key is pressed.
3. The recorded keystrokes will be saved in encrypted form in `input.py`.

## Decrypting the Keystrokes

1. Use the `decrypt.py` script to decrypt the keystrokes:
   ```bash
   python decrypt.py
   ```
2. Follow the prompts to provide the encryption key and retrieve the recorded keystrokes in plain text.

## Notes

- Ensure that this tool is used responsibly and only with proper authorization. Unauthorized use is illegal and unethical.
- Keep the encryption key secure to prevent unauthorized decryption of the recorded keystrokes.

## To-Do

- Implement automatic upload of the encrypted file to Dropbox.
- Add more encryption options for enhanced security.

## Disclaimer

This project is for educational purposes only. The developers are not responsible for any misuse of this tool.

---

### Contribution

Feel free to fork the repository and submit pull requests to enhance functionality or fix issues..

