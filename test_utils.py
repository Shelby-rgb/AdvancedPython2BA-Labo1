# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(0), 1)
        self.assertEqual(utils.fact(1), 1)
        self.assertEqual(utils.fact(5), 120)

    def test_roots(self):
        self.assertEqual(utils.roots(2, 4, 0),(0, -2 ))
        self.assertEqual(utils.roots(-1, 0, 1),(-1, 1))
        self.assertEqual(utils.roots(1, -4, 4),(2))
        self.assertEqual(utils.roots(1, 2, 3),())
    
    def test_integrate(self):
        self.assertEqual(utils.integrate("2*x", -4, 2), -12)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())