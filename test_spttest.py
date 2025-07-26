import unittest
from spttest import countc

class TestCountC(unittest.TestCase):

    def test_count_existing_char(self):
        self.assertEqual(countc("banana", "a"), 3)

    def test_count_non_existing_char(self):
        self.assertEqual(countc("hello", "z"), 0)

    def test_count_upper_lower_case(self):
        self.assertEqual(countc("Hello", "h"), 0)  # case-sensitive

    def test_empty_string(self):
        self.assertEqual(countc("", "a"), 0)

    def test_special_char(self):
        self.assertEqual(countc("a!a@a", "@"), 1)

if __name__ == "__main__":
    unittest.main()
