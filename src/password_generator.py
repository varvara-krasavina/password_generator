import secrets
import string

ALPHABET = string.ascii_letters + string.digits + string.punctuation


class Generator:

    def __init__(self, alphabet: str = ALPHABET):
        self.alphabet = alphabet

    def generate(self, passlen: int) -> str:
        """Generate random password

        Parameters:
        passlen (int): Password length
        chars (str): Characters to choose from, default: ascii + digits

        Returns:
        str:Generated Password
        """
        password = ''.join(
            secrets.choice(self.alphabet)
            for _ in range(passlen)
            )
        return password
