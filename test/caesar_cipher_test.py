import unittest
from src import caesar_cipher as caesar_cipher

class MyTestCase(unittest.TestCase):
    def test_moving_shift(self):
        self.assertEqual(caesar_cipher.moving_shift('I should have known that you would have a perfect answer for me!!!', 1),  ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"], 'moving_shift(caesar_cipher.moving_shift(%s, %d)' % ('I should have known that you would have a perfect answer for me!!!', 1))

    def test_demoving_shift(self):
        self.assertEqual(caesar_cipher.demoving_shift( ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"], 1), 'I should have known that you would have a perfect answer for me!!!', 'demoving_shift(caesar_cipher.moving_shift([%s, %s, %s, %s, %s], %d)' % ("J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!", 1))

  
if __name__ == '__main__':
    unittest.main()
