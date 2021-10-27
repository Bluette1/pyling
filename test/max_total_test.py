import unittest
from src import max_total as maxtotal

class MyTestCase(unittest.TestCase):
    def test_maxtotal(self):
        self.assertEqual(maxtotal(20,[2,4]), 20, 'maxtotal(%d, [%d, %d])' % (20, 2, 4))
        self.assertEqual(maxtotal(25,[2,3]), 25, 'maxtotal(%d, [%d, %d])' % (25, 2, 3))
        self.assertEqual(maxtotal(91,[6]), 90, 'maxtotal(%d, [%d])' % (91, 6))
        self.assertEqual(maxtotal(43,[2, 5]), 43, 'maxtotal(%d, [%d, %d])' % (43, 2, 5))
        self.assertEqual(maxtotal(100,[6,3,2]), 100, 'maxtotal(%d, [%d, %d, %d])' % (100, 6, 3, 2))
        self.assertEqual(maxtotal(100,[6,3]), 99, 'maxtotal(%d, [%d, %d])' % (100, 6, 3))

if __name__ == '__main__':
    unittest.main()
