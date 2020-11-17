from pretty_bad_protocol import gnupg
import requests
from pathlib import Path
import hashlib
import glob

import hashlib
from utils import passwordHasBeenFound

def main():
    gpg = gnupg.GPG(homedir='/home/aaron/.gnupg', verbose=True)

    pathToPasswordDir = Path("/home/aaron/Code/Python/Security-Utils/files").absolute()

    passwords = []

    for filePathEl in pathToPasswordDir.iterdir():
        with open(filePathEl, 'rb') as file:
            passwords.append( gpg.decrypt_file(file))

    
    listofFound = []
    for passwordStrEl in passwords:
        hasBeenFound = passwordHasBeenFound(str(passwordStrEl))
        if hasBeenFound:
            listofFound.append(str(passwordStrEl))
        print(passwordStrEl)

if __name__ == "__main__":
    main()
