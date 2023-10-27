import unittest
from Homework_4 import *

class TestingTernarySearch(unittest.TestCase):
    
    def test_doesExist(self):
        lst = [1, 10, 23, 48, 99, 200, 323]
        self.assertTrue(doesExist(lst, 99))
        self.assertFalse(doesExist(lst, 500))
        self.assertFalse(doesExist([], 50))

    def test_computeMidpoints(self):
        self.assertEqual((1, 2), computeMidpoints(0, 3))
        self.assertEqual((0, 1), computeMidpoints(0, 2))

    def test_ternarySearch(self):
        lst = [1, 10, 23, 48, 99, 200, 323]
        self.assertEqual(4, ternarySearch(lst, 99))
        self.assertEqual(-1, ternarySearch(lst, 500))
        self.assertEqual(-1, ternarySearch([], 50))

    def test_gameRanking(self):
        scores = [323, 200, 99, 48, 23, 10, 1]
        self.assertEqual((3, 101), gameRanking(scores, 99))
        self.assertEqual((1, 0), gameRanking(scores, 323))
        self.assertEqual((-1, -1), gameRanking(scores, 500))

if __name__ == '__main__':
    unittest.main()


"""
by Francois
  _____ ____  ___   ____________
  / ___// __ \/   | / ____/ ____/
  \__ \/ /_/ / /| |/ /   / __/   
 ___/ / ____/ ___ / /___/ /___   
/____/_/   /_/  |_\____/_____/  
""" 

