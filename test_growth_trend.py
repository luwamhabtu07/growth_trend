import unittest
from growth_trend import sortedSquares

class TestSortedSquares(unittest.TestCase):
    # Normal test case
    def test_example1(self):
        self.assertEqual(sortedSquares([-5,-2,0,3,10]), [0,4,9,25,100])
    
    def test_example2(self):
        self.assertEqual(sortedSquares([-8,-3,2,4,12]),[4,9,16,64,144])

    def test_all_negative(self):
        self.assertEqual(sortedSquares([-7,-5,-3,-1]),[1,9,25,49])

    #Edge test case
    def test_all_positive(self):
        self.assertEqual(sortedSquares([1,2,3,4]),[1,4,9,16])

    def test_single_element(self):
        self.assertEqual(sortedSquares([-4]),[16])

    def test_empty(self):
        self.assertEqual(sortedSquares([]),[])

if __name__ == "__main__":
    unittest.main()
    