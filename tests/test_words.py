import unittest

from textkit import word_count


class TestWordCount(unittest.TestCase):
    def test_simple_sentence(self):
        self.assertEqual(word_count("오픈소스 소프트웨어 강좌"), 3)

    def test_single_word(self):
        self.assertEqual(word_count("Git"), 1)

    # 이슈를 해결할 때: 버그를 재현하는 테스트를 이 아래에 추가하세요.


if __name__ == "__main__":
    unittest.main()
