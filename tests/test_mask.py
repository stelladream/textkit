import unittest

from textkit import mask_email


class TestMaskEmail(unittest.TestCase):
    def test_long_id(self):
        self.assertEqual(mask_email("alice@example.com"), "al***@example.com")

    # 이슈를 해결할 때: 버그를 재현하는 테스트를 이 아래에 추가하세요.


if __name__ == "__main__":
    unittest.main()
