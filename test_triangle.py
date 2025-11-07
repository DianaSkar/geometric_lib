import unittest
import math
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(10, 5), 25)
        self.assertEqual(area(6, 4), 12)
        self.assertEqual(area(0, 5), "FAIL")
    
    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(0, 0, 0), "FAIL")
        self.assertEqual(perimeter(4, 8, 11), 23)