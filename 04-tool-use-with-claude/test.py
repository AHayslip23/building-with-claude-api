import unittest
import math
from main import calculate_pi_to_fifth_digit


class TestCalculatePiToFifthDigit(unittest.TestCase):
    """Test suite for the calculate_pi_to_fifth_digit function."""

    EXPECTED_PI = 3.14159  # pi rounded to 5 decimal places

    def test_return_value_equals_pi_to_fifth_digit(self):
        """The function must return exactly 3.14159."""
        result = calculate_pi_to_fifth_digit()
        self.assertEqual(result, self.EXPECTED_PI)

    def test_return_type_is_float(self):
        """The return type must be a float."""
        result = calculate_pi_to_fifth_digit()
        self.assertIsInstance(result, float)

    def test_fifth_decimal_place_is_correct(self):
        """The digit at the fifth decimal place must be 9."""
        result = calculate_pi_to_fifth_digit()
        fifth_decimal = int(result * 100000) % 10
        self.assertEqual(fifth_decimal, 9)

    def test_integer_part_is_three(self):
        """The integer part of pi must be 3."""
        result = calculate_pi_to_fifth_digit()
        self.assertEqual(int(result), 3)

    def test_within_tolerance_of_math_pi(self):
        """Result must be within 0.000005 of math.pi (half a ULP at 5 d.p.)."""
        result = calculate_pi_to_fifth_digit()
        self.assertAlmostEqual(result, math.pi, places=5)

    def test_no_more_than_five_decimal_places(self):
        """Result must not carry significant digits beyond 5 decimal places."""
        result = calculate_pi_to_fifth_digit()
        # Multiply by 1e5, round, then check the remainder is negligible
        scaled = result * 10 ** 5
        self.assertAlmostEqual(scaled, round(scaled), places=5)

    def test_result_is_greater_than_three(self):
        """Pi is always greater than 3."""
        result = calculate_pi_to_fifth_digit()
        self.assertGreater(result, 3)

    def test_result_is_less_than_four(self):
        """Pi is always less than 4."""
        result = calculate_pi_to_fifth_digit()
        self.assertLess(result, 4)


if __name__ == "__main__":
    unittest.main()
