"""Test challenge 2"""
import os
import sys
import unittest
from datetime import datetime

sys.path.append(os.getcwdb().decode("utf-8"))

from app.challenge_2 import get_season


class TestOrdStatus(unittest.TestCase):
    def test_get_season_spring(self):
        date = datetime(2019, 3, 30)

        season = get_season(date)
        self.assertEqual(season, "SPRING", "Should be SPRING")

    def test_get_season_summer(self):
        date = datetime(2019, 7, 10)

        season = get_season(date)
        self.assertEqual(season, "SUMMER", "Should be SUMMER")

    def test_get_season_fall(self):
        date = datetime(2019, 10, 15)

        season = get_season(date)
        self.assertEqual(season, "FALL", "Should be FALL")

    def test_get_season_winter(self):
        date = datetime(2019, 1, 1)

        season = get_season(date)
        self.assertEqual(season, "WINTER", "Should be WINTER")


if __name__ == "__main__":
    unittest.main()
