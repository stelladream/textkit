import unittest

from textkit import count_hangul


class TestCountHangul(unittest.TestCase):
    def test_mixed_text(self):
        self.assertEqual(count_hangul("Git 과 GitHub"), 1)

    def test_only_hangul(self):
        self.assertEqual(count_hangul("가나다"), 3)

    # 이슈를 해결할 때: 버그를 재현하는 테스트를 이 아래에 추가하세요.


if __name__ == "__main__":
    unittest.main()
