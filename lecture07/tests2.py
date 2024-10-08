import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):
        self.assertEqual((2+3), 5)
        self.assertEqual(0+3, 3)
        
    def testMultiply(self):
        self.assertEqual(1*1, 1)
        self.assertEqual(6*7, 42)
        
if __name__ == '__main__':
    unittest.main()
        