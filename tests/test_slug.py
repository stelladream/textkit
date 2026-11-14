import unittest

from textkit import slugify


class TestSlugify(unittest.TestCase):
    def test_two_words(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_korean_is_kept(self):
        self.assertEqual(slugify("오픈소스"), "오픈소스")

    # 이슈를 해결할 때: 버그를 재현하는 테스트를 이 아래에 추가하세요.


if __name__ == "__main__":
    unittest.main()
