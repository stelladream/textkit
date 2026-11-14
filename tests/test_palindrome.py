import unittest

from textkit import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_simple_word(self):
        self.assertTrue(is_palindrome("level"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("github"))

    # 이슈를 해결할 때: 버그를 재현하는 테스트를 이 아래에 추가하세요.


if __name__ == "__main__":
    unittest.main()
