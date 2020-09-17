import random
import string

CHARS = string.ascii_letters + string.digits + string.punctuation


class Generator:

    def __init__(self):
        pass

    def generate(self, passlen: int, chars: str = CHARS) -> str:
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
