import random
import string
import argparse

CHARS = string.ascii_uppercase + string.ascii_lowercase + string.digits

def gen_password(passlen: int, chars: str = CHARS) -> str:
    """Generate random password

    Parameters:
    passlen (int): Password length
    chars (str): Characters to choose from, default: ascii + digits

    Returns:
    str:Generated Password
    """

    password = ''.join(
        random.choice(chars)
        for _ in range(passlen)
    )

    return password

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('passlen', type=int, nargs=1, help='Required, password length')
    parser.add_argument('-ch', '--chars', type=str, nargs=1, help='Optional, characters to choose from, default: ascii + digits')

    passlen = parser.parse_args().passlen[0]
    chars = parser.parse_args().chars

    if chars:
        password = gen_password(passlen, chars=chars[0])
    else:
        password = gen_password(passlen)

    print(password)
