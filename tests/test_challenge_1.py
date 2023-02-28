"""Test challenge 1"""
import os
import sys
import unittest

sys.path.append(os.getcwdb().decode("utf-8"))

import pandas as pd

from app.challenge_1 import get_status


class TestOrdStatus(unittest.TestCase):
    def test_get_status_pending(self):
        test_df = pd.DataFrame(
            {
                "order_number": ["123", "123", "123"],
                "status": ["SHIPPED", "PENDING", "CANCELLED"],
            }
        )
        status = get_status(test_df)
        self.assertEqual(status, "PENDING", "Should be PENDING")

    def test_get_status_shipped(self):
        test_df = pd.DataFrame(
            {
                "order_number": ["123", "123", "123"],
                "status": ["SHIPPED", "SHIPPED", "CANCELLED"],
            }
        )
        status = get_status(test_df)
        self.assertEqual(status, "SHIPPED", "Should be SHIPPED")

    def test_get_status_cancelled(self):
        test_df = pd.DataFrame(
            {
                "order_number": ["123", "123", "123"],
                "status": ["CANCELLED", "CANCELLED", "CANCELLED"],
            }
        )
        status = get_status(test_df)
        self.assertEqual(status, "CANCELLED", "Should be CANCELLED")


if __name__ == "__main__":
    unittest.main()
