import unittest
from pagination import parse_limit, parse_page


class TestLimit(unittest.TestCase):
    def test_default(self):
        self.assertEqual(parse_limit(None), 20)

    def test_bounds(self):
        self.assertEqual(parse_limit('1'), 1)
        self.assertEqual(parse_limit('100'), 100)

    def test_zero_invalid(self):
        with self.assertRaises(ValueError):
            parse_limit('0')

    def test_above_max_invalid(self):
        with self.assertRaises(ValueError):
            parse_limit('101')

    def test_text_invalid(self):
        with self.assertRaises(ValueError):
            parse_limit('abc')


class TestPage(unittest.TestCase):
    def test_default(self):
        self.assertEqual(parse_page(None), 1)

    def test_valid(self):
        self.assertEqual(parse_page('1'), 1)
        self.assertEqual(parse_page('5'), 5)

    def test_invalid(self):
        for value in ('0', '-1', 'abc'):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_page(value)


if __name__ == '__main__':
    unittest.main()
