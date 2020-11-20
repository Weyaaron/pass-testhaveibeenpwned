from pathlib import Path

from src.utils import extract_file_paths, extract_plain_text_passwort_from_pgp_file, check_password


def main():
    gpg_files = extract_file_paths(Path().home().joinpath("./.password-store"))

    passwords_found = []
    for file_el in gpg_files:
        plain_text_pass_word = extract_plain_text_passwort_from_pgp_file(file_el)
        result = check_password(plain_text_pass_word)
        if result:
            passwords_found.append((file_el.name, plain_text_pass_word))

    for el in passwords_found:
        print(el)


if __name__ == "__main__":
    main()
