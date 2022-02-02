import unittest
from src import sum_max

class MyTestCase(unittest.TestCase):
    def test_sum_max(self):
        self.assertEqual(sum_max([1, 6, 0, 7, 4, 2]), 13, 'sum_max([%d, %d, %d, %d, %d, %d])' % (1, 6, 0, 7, 4, 2))

if __name__ == '__main__':
    unittest.main()
