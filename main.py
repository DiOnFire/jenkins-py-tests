import unittest


class TestCalcMin(unittest.TestCase):
    def test_calc_min_1(self):
        res = calc_min(1, 2, 3)
        self.assertEqual(res, 1)

    def test_calc_min_2(self):
        res = calc_min(2, 1, 3)
        self.assertEqual(res, 1)

    def test_calc_min_3(self):
        res = calc_min(3, 2, 1)
        self.assertEqual(res, 1)


def calc_min(a: int, b: int, c: int) -> int:
    if a < b and a < c:
        return a
    if b < a and b < c:
        return b
    return c