from unittest import TestCase

from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(16, 3, '+')
        self.assertEqual(19, result)

    def test_minus(self):
        result = operations(16, 3, '-')
        self.assertEqual(13, result)

    def test_multiply(self):
        result = operations(16, 3, '*')
        self.assertEqual(48, result)

    def test_divide(self):
        result = operations(15, 3, '//')
        self.assertEqual(5, result)
