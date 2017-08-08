import unittest
from Sumador import *
from Perceptron import *

class MyTestCase(unittest.TestCase):

    def test_or(self):
        or_perceptron = Perceptron([2, 2], -1)
        self.assertEqual(or_perceptron.output([1,1]), 1)
        self.assertEqual(or_perceptron.output([0, 0]), 0)
        self.assertEqual(or_perceptron.output([0, 1]), 1)

    def test_nand(self):
        nand_perceptron = Perceptron( [-2, -2], 3)
        self.assertEqual(nand_perceptron.output([1, 1]), 0)
        self.assertEqual(nand_perceptron.output([0, 1]), 1)
        self.assertEqual(nand_perceptron.output([1, 0]), 1)
        self.assertEqual(nand_perceptron.output([0, 0]), 1)

    def test_and(self):
        and_perceptron = Perceptron([2, 2], -3)
        self.assertEqual(and_perceptron.output([1, 1]), 1)
        self.assertEqual(and_perceptron.output([0, 1]), 0)
        self.assertEqual(and_perceptron.output([1, 0]), 0)
        self.assertEqual(and_perceptron.output([1, 0]), 0)

    def test_sumador(self):
        sumador = Sumador()
        suma_00 = sumador.sumar([0, 0])
        suma_10 = sumador.sumar([1, 0])
        suma_01 = sumador.sumar([0, 1])
        suma_11 = sumador.sumar([1, 1])

        #suma_XX[0] => sum
        #suma_XX[1] => carry bit
        self.assertEqual(suma_00[0], 0)
        self.assertEqual(suma_00[1], 0)

        self.assertEqual(suma_10[0], 1)
        self.assertEqual(suma_10[1], 0)

        self.assertEqual(suma_01[0], 1)
        self.assertEqual(suma_01[1], 0)

        self.assertEqual(suma_11[0], 0)
        self.assertEqual(suma_11[1], 1)





if __name__ == '__main__':
    unittest.main()
