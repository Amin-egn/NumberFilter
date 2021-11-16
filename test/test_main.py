# standard
import unittest
from random import randint
# internal
from src.filter import get_input



test_mobile_nums = list()
for i in range(10):
    test_mobile_nums.append(str(randint(9000000000, 9999999999)) + '+98')

test_city_nums = list()
for i in range(10):
    test_city_nums.append(str(randint(1000000000, 8999999999)) + '98')


class TestNumber(unittest.TestCase):
    """Test Number Filter"""
    def test_mobile(self):
        expected_result = 2
        for num in test_mobile_nums:
            result = get_input(num)
            self.assertEqual(expected_result, result)

    def test_city(self):
        expected_result = 1
        for num in test_city_nums:
            result = get_input(num)
            self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
