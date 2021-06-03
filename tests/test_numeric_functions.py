import unittest
import module.numeric_functions as numeric_functions


class TestNumericFunctions(unittest.TestCase):
	def test_sum_numbers_2(self):
		self.assertEqual(numeric_functions.sum_numbers(1, 2), 3)

	def test_sum_numbers_3(self):
		self.assertEqual(numeric_functions.sum_numbers(1, 2, 3), 6)

	def test_sum_numbers_multiple_cases(self):
		test_cases = [
			("2 numbers", (1, 2), 3),
			("3 numbers", (1, 2, 3), 6)
		]
		for message, case, expected in test_cases:
			with self.subTest(msg=message):
				self.assertEqual(numeric_functions.sum_numbers(*case), expected)
