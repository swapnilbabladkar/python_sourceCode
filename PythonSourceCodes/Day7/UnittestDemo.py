# Unittest Demo
from Fibonacci import fib
import unittest

class FibTest(unittest.TestCase):
    def testValues(self):
        self.assertEqual(fib(1),1)
        self.assertEqual(fib(8),21)
        self.assertEqual(fib(30),832040)
        self.assertEqual(fib(88),1100087778366101931L)
        
    

if __name__ == "__main__":
    unittest.main()
