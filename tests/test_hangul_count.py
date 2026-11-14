import unittest

from textkit import count_hangul


class TestCountHangul(unittest.TestCase):
    def test_mixed_text(self):
        self.assertEqual(count_hangul("Git 과 GitHub"), 1)

    def test_only_hangul(self):
        self.assertEqual(count_hangul("가나다"), 3)

    def test_last_syllable_is_counted(self):
        self.assertEqual(count_hangul("힣"), 1)

    def test_range_boundaries_are_inclusive(self):
        self.assertEqual(count_hangul("가힣"), 2)


if __name__ == "__main__":
    unittest.main()
