import hashlib

import requests


def passwordHasBeenFound(passWordArg:str)-> bool:
    hashObject = hashlib.sha1(bytes(passWordArg, "utf8"))
    hexDig = hashObject.hexdigest() [0:5]

    apiResult = requests.get("https://api.pwnedpasswords.com/range/" + hexDig)

    for hash in apiResult.text.split("\n"):
        if hexDig[5:len(hexDig)].lower() ==  hash.split(":")[0].lower():
            return True
    return False


