import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario

    def test_list_of_two_prices_no_discount(self):
        prices = [10,9]
        expected_discount = 0
        calculated_discount = discount(prices)
        self.assertEqual(expected_discount, calculated_discount)

    def test_list_of_one_price_no_discount(self):
        prices = [11]
        expected_discount = 0
        calculated_discount = discount(prices)
        self.assertEqual(expected_discount, calculated_discount)

    def test_list_contains_non_integer_values_raise_exception(self):
        prices = ['String', 10, 7]
        
        with self.assertRaises(Exception):
            discount(prices)

    def test_argument_is_list(self):
        self.fail()

    def test_argument_not_list_raise_exception(self):
        self.fail()

    def test_list_contains_numbers_greater_than_zero(self):
        self.fail

    def test_list_contains_zero_or_negative_numbers_raise_exception(self):
        self.fail()

    def test_list_not_empty(self):
        self.fail()

    def test_list_empty_raise_exception(self):
        self.fail()
    
    def test_discount_with_decimal_prices(self):
        self.fail()

    def test_discount_with_none(self):
        self.fail()

    def test_discount_with_duplicate_lowest_prices(self):
        self.fail()

if __name__ == '__main__':
    unittest.main()