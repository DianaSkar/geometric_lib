import unittest
import math
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5, 2), 10)
        self.assertEqual(area(3, 18), 54)
        self.assertEqual(area(0, 5), "FAIL")
    
    def test_perimeter(self):
        self.assertEqual(perimeter(5, 2), 14)
        self.assertEqual(perimeter(3, 18), 42)
        self.assertEqual(perimeter(0, 5), "FAIL")