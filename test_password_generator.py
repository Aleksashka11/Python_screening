from password_generator import generate, strong_password
import unittest
import string


class MyTestCase(unittest.TestCase):
    def test_strong_password(self):
        password = strong_password()
        bool = False
        for char in password:
            if char in string.punctuation:
                punc = True
                break
        if any(char.islower() for char in password)\
                and any(char.isupper() for char in password)\
                and any(char.isdigit() for char in password)\
                and punc == True\
                and len(password) >= 14:
            bool = True
        self.assertEqual(bool, True)


if __name__ == '__main__':
    unittest.main()
