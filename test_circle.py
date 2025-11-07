import unittest
import math
from circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(7) ,math.pi * 49)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(0.5), math.pi * 0.25)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5)
        self.assertAlmostEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(3.5), 2 * math.pi * 3.5)
