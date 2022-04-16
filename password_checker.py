import re
import string
import sys


def weak_password_decorator(function):
    """ Decorator has been written to detect errors in the weak password.
        Dictionary stores errors as keys and regex patterns to check for as values.
        Iterating through dictionary in order to print errors occured.
    """
    def wrapper(password):
        func = function(password)
        dict = {
            "contain both lowercase and uppercase characters": r'\w*[A-Z][a-z]\w*',
            "contain digits": r'\w*\d\w*',
            "contain at least one punctuation character":
                r'\w*[!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]\w*',
            "be at 14 characters long": r'^.{14,}$'
        }
        [print('Password must {}'.format(key)) for key, value in dict.items()
         if re.search(value, password) is None]
    return wrapper


@weak_password_decorator
def check_the_strength(password):
    """Function to check for weak and strong passwords"""
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~])(\s*)[A-Za-z\d\s*!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]{14,}$"
    compiled_regex = re.compile(regex)
    result = re.search(compiled_regex, password)
    if result:
        print("Strong password")
    else:
        print("Weak password")


if __name__ == '__main__':
    check_the_strength(''.join(value for id, value in enumerate(sys.argv) if id > 0))
