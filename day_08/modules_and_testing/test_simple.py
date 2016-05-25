from mark_mod.simple import positive_divide
import unittest

# define a testing class
class TestPositiveDivide(unittest.TestCase):
    def setUp(self):  # common setup code
        pass # e.g., print "running setup!"
    def test_basic(self):
        # Test with simple integer arguments
        g = positive_divide(40,10)
        self.assertEqual(g,4)
    def test_negative(self):
        self.assertRaises(ValueError, positive_divide, 8, -2)
        self.assertRaises(ValueError, positive_divide, -2, 8)
    def test_zero_denom(self):
        self.assertRaises(ZeroDivisionError, positive_divide, 10, 0)
    def test_big(self):
        # Test with long integers
        q = positive_divide(23748928388, 6723884)
        self.assertEqual(q,3532)
    def tearDown(self): # common tear down code
        pass # e.g., print "tearing down ... (am i angry or what?)"

if __name__=="__main__":
    unittest.main()
