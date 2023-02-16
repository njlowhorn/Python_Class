# Python V 3.11.1

import unittest


class TestSum(unittest.TestCase):
    def test_sum(self):
        assert sum([1, 2, 3]) == 6, "Should be 6"
        #assert sum([1, 1, 1]) == 6, "Should be 6"

    def test_sum_tuple(self):
        assert sum([1, 2, 2]) == 6, "Should be 6"

if __name__ == "__main__":
    unittest.main()