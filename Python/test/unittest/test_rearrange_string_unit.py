import unittest
from src.rearrange_string import rearrange_string


class TestRearrangeString(unittest.TestCase):

    def test_rearrange_string(self):
        self.assertEqual(rearrange_string("AbC123DeF"), "fedcba")
        self.assertEqual(rearrange_string("Hello123WORLD"), "dlrowolleh")
        self.assertEqual(rearrange_string("123"), "")
        self.assertEqual(rearrange_string(""), "")


if __name__ == "__main__":
    unittest.main()
