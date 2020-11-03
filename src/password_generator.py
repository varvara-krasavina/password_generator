import logging

import secrets
import string

ALPHABET = string.ascii_letters + string.digits + string.punctuation


class Generator:
    """Generates a random password of given length.

    """

    def __init__(self, alphabet: str = ALPHABET):
        self.alphabet = alphabet

    def generate(self, passlen: int) -> str:
        """Generate random chars and form a string.
        Default alphabet is ascii + digits + punctuation marks.

        Parameters:
        passlen (int): Password length

        Returns:
        {
        response (str or None): Password
        error (str, optional): Error description
        }
        """

        try:
            password = ''.join(
                secrets.choice(self.alphabet)
                for _ in range(passlen)
                )
            return {'response': password}

        except Exception as e:
            error_msg = 'Oops! An error occurred: %s.' % e
            logging.error(error_msg)
            return {'response': None, 'error': error_msg}
