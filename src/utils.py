import hashlib
from pathlib import Path

import requests
from pretty_bad_protocol import gnupg


def extract_file_paths(base_path: Path) -> list:
    '''Collects the filepaths of the pgp files'''
    result = []
    for file_el in base_path.iterdir():
        if file_el.is_dir():
            result.extend(extract_file_paths(file_el))
        if ".gpg" in file_el.name:
            result.append(file_el)
    return result


def extract_plain_text_passwort_from_pgp_file(file_path: Path) -> str:
    gpg = gnupg.GPG(homedir='~/.gnupg')

    with open(file_path, 'rb') as file_handle:
        try:
            plain_file_content = gpg.decrypt_file(file_handle)
        except ValueError:
            pass

    return str(plain_file_content).strip("\n")


def check_password(plaintext_password: str) -> bool:
    hash_object = hashlib.sha1(bytes(plaintext_password, "utf8"))

    hex_digest = hash_object.hexdigest()
    api_result = requests.get("https://api.pwnedpasswords.com/range/" + str(hex_digest[0:5]))

    for hash_el in api_result.text.split("\n"):
        hash_value = hex_digest[0:5] + hash_el.split(":")[0].lower()

        if hex_digest == hash_value:
            return True

    return False
