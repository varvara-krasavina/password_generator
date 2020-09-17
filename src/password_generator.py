import secrets
import string

CHARS = string.ascii_letters + string.digits + string.punctuation


class Generator:

    def __init__(self, chars: str = CHARS):
        self.default_chars = chars

    def generate(self, passlen: int) -> str:
        """Generate random password

        Parameters:
        passlen (int): Password length
        chars (str): Characters to choose from, default: ascii + digits

        Returns:
        str:Generated Password
        """
        password = ''.join(
            secrets.choice(self.default_chars)
            for _ in range(passlen)
            )
        return password
