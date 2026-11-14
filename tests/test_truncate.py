import unittest

from textkit import truncate


class TestTruncate(unittest.TestCase):
    def test_short_text_is_unchanged(self):
        self.assertEqual(truncate("짧은 글", 10), "짧은 글")

    def test_exact_width_is_unchanged(self):
        self.assertEqual(truncate("12345", 5), "12345")

    # 이슈를 해결할 때: 버그를 재현하는 테스트를 이 아래에 추가하세요.


if __name__ == "__main__":
    unittest.main()
