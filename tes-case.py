"""
Module test_case
"""

import unittest
from aosnifds import add_numbers

class TestTechWeekSession(unittest.TestCase):
    """Unit tests for Tech Week Session"""

    def test_add_numbers(self):
        """Test the add_numbers function"""
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
