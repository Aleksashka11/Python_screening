import string
import random
import secrets
from itertools import chain


def generate(elements):
    """Function that generates a list of secure random elements"""
    return [secrets.choice(elements) for i in range(random.randrange(3, 5, 1))]


def strong_password():
    """ Function applies generate() to every item in the list.
        Then shuffles all the elements."""
    password = []
    password.append(string.ascii_lowercase)
    password.append(string.ascii_uppercase)
    password.append(string.punctuation)
    password.append(string.digits)
    gen_char = list((chain.from_iterable(list(map(generate, password)))))
    random.shuffle(gen_char)
    return ''.join(list(gen_char))


if __name__ == '__main__':
    print(strong_password())
