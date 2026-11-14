import unittest

from textkit import reading_time


class TestReadingTime(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(reading_time(""), 0)

    def test_exact_minutes(self):
        self.assertEqual(reading_time("단어 " * 400), 2)

    # 이슈를 해결할 때: 버그를 재현하는 테스트를 이 아래에 추가하세요.


if __name__ == "__main__":
    unittest.main()
