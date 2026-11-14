import unittest

from textkit import normalize_spaces


class TestNormalizeSpaces(unittest.TestCase):
    def test_already_normal(self):
        self.assertEqual(normalize_spaces("오픈소스 기여"), "오픈소스 기여")

    def test_double_space(self):
        self.assertEqual(normalize_spaces("오픈소스  기여"), "오픈소스 기여")

    # 이슈를 해결할 때: 버그를 재현하는 테스트를 이 아래에 추가하세요.


if __name__ == "__main__":
    unittest.main()
