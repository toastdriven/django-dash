import hashlib
import random


VALID_CHOICES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(
    ""
)


def generate_code(choices=VALID_CHOICES, length=16):
    """
    Generates a random code, typically for verifications.

    This isn't cryptographically secure & should only be used when there's a
    second piece of information to verify with.

    Args:
        choices (list): A list of single character choices to create the code
            from. Default is `VALID_CHOICES`.
        length (int): The desired length of the code. Default is `16`.

    Returns:
        str: The generated code.
    """
    bits = []

    for _ in range(length):
        choice = random.choice(choices)
        bits.append(choice)

    return "".join(bits)


def generate_hash(to_hash, length=8, salt=""):
    """
    Generates a salted hash of the provided data, then returns a fragment of
    the hash.

    Useful for things that need to be more secure than just `generate_code`.

    Under the hood, this uses SHA-1 for hashing.
    **NOT GOOD ENOUGH FOR SENSITIVE DATA!**

    Args:
        to_hash (str): The data to generate the hash off of.
        length (int): The desired length of the code. Default is `8`.
        salt (str): An (optional) salt to further obscure the original data.
            Default is `""`, for no salt.

    Returns:
        str: The generated hash fragment.
    """
    hashed = hashlib.sha1(to_hash + salt).hexdigest()
    return str(hashed)[:length]
