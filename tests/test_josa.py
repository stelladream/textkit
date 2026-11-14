import unittest

from textkit import add_josa


class TestAddJosa(unittest.TestCase):
    def test_eul_reul(self):
        self.assertEqual(add_josa("사과", "을/를"), "사과를")
        self.assertEqual(add_josa("책", "을/를"), "책을")

    def test_i_ga(self):
        self.assertEqual(add_josa("책", "이/가"), "책이")

    def test_euro_ro_without_batchim(self):
        self.assertEqual(add_josa("학교", "으로/로"), "학교로")

    def test_unsupported_pair(self):
        with self.assertRaises(ValueError):
            add_josa("책", "에/에게")

    # 이슈를 해결할 때: 버그를 재현하는 테스트를 이 아래에 추가하세요.


if __name__ == "__main__":
    unittest.main()
