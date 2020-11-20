import sys
from pathlib import Path

from src.utils import extract_file_paths, extract_plain_text_passwort_from_pgp_file, check_password


def main():
    print("To enable passwort-printing, run with -v")

    gpg_files = extract_file_paths(Path().home().joinpath("./.password-store"))

    passwords_found = []
    password_found = False
    for file_el in gpg_files:
        plain_text_pass_word = extract_plain_text_passwort_from_pgp_file(file_el)
        result = check_password(plain_text_pass_word)
        if result:
            passwords_found.append((file_el.name, plain_text_pass_word))
        password_found = passwords_found or result

    if "-v" in sys.argv:
        print("Verbosity is set, printing the plaintext-passwords")

        for el in passwords_found:
            print(el)
        exit(0)

    if password_found:
        print("Atleast one password has been found")
        exit(0)
    else:
        print("No passwort has been found")
        exit(0)


if __name__ == "__main__":
    main()
