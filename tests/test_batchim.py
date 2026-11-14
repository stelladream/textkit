import unittest

from textkit import has_batchim


class TestHasBatchim(unittest.TestCase):
    def test_with_batchim(self):
        self.assertTrue(has_batchim("강"))

    def test_without_batchim(self):
        self.assertFalse(has_batchim("가"))

    # 이슈를 해결할 때: 버그를 재현하는 테스트를 이 아래에 추가하세요.


if __name__ == "__main__":
    unittest.main()
