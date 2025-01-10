# Keylogger with Dropbox Integration

This project is a Python-based keylogger that records keystrokes, encrypts them, and uploads the encrypted logs to Dropbox. It uses the following libraries:

- `pynput` for capturing keyboard input.
- `cryptography` for encryption using the `Fernet` symmetric encryption method.
- `dropbox` for uploading files to a Dropbox account.

## Features
- Logs all keyboard input into a file (`input.txt`) in encrypted form.
- Generates an encryption key (`key.txt`) to decrypt the logged data.
- Automatically uploads the log file and encryption key to Dropbox when the `Esc` key is pressed.

## Prerequisites
- Python 3.6 or higher
- Dropbox account
- Dropbox API Access Token

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/keylogger-with-dropbox.git
   cd keylogger-with-dropbox
   ```

2. **Install Dependencies**
   ```bash
   pip install pynput cryptography dropbox
   ```

3. **Set Your Dropbox Access Token**
   Replace `ACCESS_TOKEN` in the script with your Dropbox API access token. You can generate one from the [Dropbox App Console](https://www.dropbox.com/developers/apps).

## Usage

1. **Run the Script**
   ```bash
   python keylogger.py
   ```

2. **Press Keys**
   - The script will log all keys pressed and encrypt them.
   - Special keys like `Enter` and `Space` are handled appropriately.

3. **Stop Logging**
   - Press the `Esc` key to stop the keylogger.
   - The script will upload the following files to Dropbox:
     - `input.txt` (the encrypted log file)
     - `key.txt` (the encryption key file)

## File Details
- **`input.txt`**: Contains encrypted logs of keyboard input.
- **`key.txt`**: Contains the encryption key required to decrypt `input.txt`.

## Security
- Logs are encrypted using `cryptography.fernet` to ensure data security.
- Do not share the `key.txt` file with unauthorized individuals, as it can be used to decrypt the logged data.

## Notes
- Ensure you have a stable internet connection for Dropbox uploads.
- Test the script in a controlled environment, as keylogging can be considered malicious behavior if used unethically.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

## Disclaimer
This tool is for educational purposes only. Unauthorized use of this script to log other individuals' activities without their consent is illegal and unethical. Use responsibly.

