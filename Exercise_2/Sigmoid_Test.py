import unittest
from Sigmoid import *

class MyTestCase(unittest.TestCase):

    def test_or(self):
        or_sigmoid = Sigmoid([20,20],-10)
        self.assertEqual(or_sigmoid.output([0, 0]) < 0.1 ,True)
        self.assertEqual(or_sigmoid.output([0, 1]) > 0.9, True)
        self.assertEqual(or_sigmoid.output([1, 0]) > 0.9, True)
        self.assertEqual(or_sigmoid.output([1, 1]) > 0.9, True)

    def test_and(self):
        and_sigmoid = Sigmoid([20, 20], -30)
        self.assertEqual(and_sigmoid.output([0, 0]) < 0.1, True)
        self.assertEqual(and_sigmoid.output([0, 1]) < 0.1, True)
        self.assertEqual(and_sigmoid.output([1, 0]) < 0.1, True)
        self.assertEqual(and_sigmoid.output([1, 1]) > 0.9, True)

    def test_nand(self):
        nand_sigmoid = Sigmoid([-20, -20], 30)
        self.assertEqual(nand_sigmoid.output([0, 0]) > 0.9, True)
        self.assertEqual(nand_sigmoid.output([1, 0]) > 0.9, True)
        self.assertEqual(nand_sigmoid.output([0, 1]) > 0.9, True)
        self.assertEqual(nand_sigmoid.output([1, 1]) < 0.1, True)


if __name__ == '__main__':
    unittest.main()
