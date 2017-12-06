import string_helper
import unittest

class BasicTestCase(unittest.TestCase):

    def test_trim_and_uppercase(self):
        value = "    Hello World   "
        expected = "HELLO WORLD"
        response = string_helper.trim_and_uppercase(value)
        self.assertEqual(response, expected)

if __name__ == '__main__':
    unittest.main()