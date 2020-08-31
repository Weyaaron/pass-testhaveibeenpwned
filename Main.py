from pretty_bad_protocol import gnupg
import requests
from pathlib import Path
import hashlib
import glob




def passwordHasBeenFound(passWordArg):
    hash_object = hashlib.sha1(bytes(passWordArg, "utf8"))
    hex_dig = hash_object.hexdigest()

    arg = hex_dig[0:5]
    apiResult = requests.get("https://api.pwnedpasswords.com/range/" + arg)

    hashList = apiResult.text.split("\n")

    for hash in hashList:
        arg1 = hex_dig[5:len(hex_dig)].lower()
        arg2 = hash.split(":")[0].lower()
        if arg1 == arg2:
            return True

    return False

def main():
    gpg = gnupg.GPG(homedir='/home/aaron/.gnupg', verbose=True)

    pathToPasswordDir = Path("/home/aaron/.password-store")

    private_keys = gpg.list_keys(True)
    print(private_keys)
    passswords = []

    filePaths = glob.glob(str(pathToPasswordDir) +"/*.gpg", recursive=True)
    for filePathEl in filePaths:
        passwordFile = open(Path(filePathEl), 'rb')
        encryptedPassword = gpg.decrypt_file(passwordFile)
        passwordFile.close()
        passswords.append(str(encryptedPassword))
    
    listofFound = []
    for passwordStrEl in passswords:
        print(passwordStrEl)
        hasBeenFound = passwordHasBeenFound(str(passwordStrEl))
        if hasBeenFound:
            listofFound.append(str(passwordStrEl))
        

if __name__ == "__main__":
    main()
