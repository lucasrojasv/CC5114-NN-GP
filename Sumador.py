from Perceptron import *
class Sumador:

    # L: Layer
    # N: Number of the Perceptron in the layer
    # Imitate the order of the image in Clase 2
    def sumar(self,input):

        nand_L1N1 = Perceptron([-2, -2], 3)
        output_L1N1 = nand_L1N1.output(input)

        nand_L2N3 = Perceptron([-2, -2], 3)
        carry_bit = nand_L2N3.output([output_L1N1,output_L1N1])


        nand_L2N1 = Perceptron([-2, -2], 3)
        output_L2N1 = nand_L2N1.output([input[0],output_L1N1])

        nand_L2N2 = Perceptron([-2, -2], 3)
        output_L2N2 = nand_L2N2.output([input[1], output_L1N1])


        nand_L3N1 = Perceptron([-2, -2], 3)
        sum = nand_L3N1.output([output_L2N1,output_L2N2])

        return [sum,carry_bit]
