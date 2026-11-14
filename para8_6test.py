import unittest
from para8_6 import *

class My_Test(unittest.TestCase):
    def test_args(self):
        self.assertEquals(adder(2, 2), 4)

if __name__ == "__main__":
    unittest.main()