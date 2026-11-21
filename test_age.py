import unittest
from datetime import date
from age import calendar_age


class AgeTests(unittest.TestCase):
    def test_calendar_boundaries(self):
        cases = [((2000, 2, 29), (2021, 2, 28), (21, 0, 0)),
                 ((2024, 1, 31), (2024, 3, 1), (0, 1, 1)),
                 ((2000, 12, 31), (2001, 1, 1), (0, 0, 1)),
                 ((2000, 5, 20), (2024, 5, 19), (23, 11, 29)),
                 ((2024, 1, 1), (2024, 1, 1), (0, 0, 0))]
        for birth, given, expected in cases:
            with self.subTest(birth=birth, given=given):
                self.assertEqual(calendar_age(date(*birth), date(*given)), expected)

    def test_reversed_dates(self):
        with self.assertRaises(ValueError):
            calendar_age(date(2024, 1, 2), date(2024, 1, 1))


if __name__ == '__main__':
    unittest.main()
