import unittest
from main import calculate_rectangle_properties

class TestRectangleCalculator(unittest.TestCase):
    def test_calculate_rectangle_properties(self):
        # Test with positive integers
        result = calculate_rectangle_properties(5, 3)
        self.assertEqual(result, (15, 16))

        # Test with the values from the main function
        result = calculate_rectangle_properties(12, 13)
        self.assertEqual(result, (156, 50))

        # Test with floating-point numbers
        result = calculate_rectangle_properties(2.5, 4.5)
        self.assertEqual(result, (11.25, 14))

        # Test with zero
        result = calculate_rectangle_properties(0, 10)
        self.assertEqual(result, (0, 20))

        # Test with negative numbers
        result = calculate_rectangle_properties(-2, 8)
        self.assertEqual(result, (-16, 12))

if __name__ == '__main__':
    unittest.main()
