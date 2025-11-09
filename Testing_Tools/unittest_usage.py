'''
Built-in unittest module usage showcase.

"unittest" has some interesting built-in methods that are worth explaining beforehand:
·assertEqual(a, b): checks whether a == b. Test passes if such condition is met.
·assertAlmostEqual(a, b): same as the method above but assuming precision differences may
happen (especially useful when floating point variables are involved).
·assertRaises(exception_type): checks that a given exception type is raised.

Note that every user-defined class meant to be using unittest's features must inherit
from unittest.TestCase. In order to run testing methods (defined within the class),
simply use unittest.main().
'''

import unittest
from math_ops import add, mul, sub, div

class TestDummyFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertAlmostEqual(add(1.2, 3.4), 4.6)
    
    def test_sub(self):
        self.assertEqual(sub(5, 2), 3)
        self.assertAlmostEqual(sub(4.3, 2.1), 2.2)
    
    def test_mul(self):
        self.assertEqual(mul(3, 6), 18)
        self.assertAlmostEqual(mul(1.2, 3.4), 4.08)
    
    def test_div(self):
        self.assertEqual(div(4, 5), 0.8)
        self.assertAlmostEqual(div(5.5, 1.1), 5.0)
        self.assertRaises(ZeroDivisionError, div, 1, 0) # Always check the syntax.

if __name__ == "__main__":
    unittest.main()