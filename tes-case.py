import unittest
from tech_week_session import add_numbers

class TestTechWeekSession(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 3), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
