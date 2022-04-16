from password_checker import weak_password_decorator, check_the_strength
from io import StringIO
import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    """Test to check the function check_the_strength()"""
    def test_check_strength(self):
        #checking the first password
        with patch('sys.stdout', new = StringIO()) as output:
            check_the_strength('The quick br0wn fox jumps 0ver the lazy d0g.')
            self.assertEqual(output.getvalue().strip(), 'Strong password')


if __name__ == '__main__':
    unittest.main()
