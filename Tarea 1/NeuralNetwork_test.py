import unittest
from NeuronLayer import *
from Neuron import *
from NeuralNetwork import *


class MyTestCase(unittest.TestCase):
    def test_or(self):
        nn = NeuralNetwork([])
        nn.createNetwork(2, 1, [2], 1)

        i1 = [0, 0]
        e1 = [0]
        i2 = [1, 0]
        e2 = [1]
        i3 = [0, 1]
        e3 = [1]
        i4 = [1, 1]
        e4 = [1]

        inputs = [i1, i2, i3, i4]
        expected_output = [e1, e2, e3, e4]

        nro_epochs = 4000
        for epoch in range(nro_epochs):
            suma_error = 0
            for i in range(len(inputs)):
                suma_error += nn.train_werror(inputs[i], expected_output[i], 0.5)

        nn.feed_forward2([0, 0])
        self.assertEqual(nn.layers[1].neurons[0].output < 0.1, True)
        nn.feed_forward2([0, 1])
        self.assertEqual(nn.layers[1].neurons[0].output> 0.9, True)
        nn.feed_forward2([1, 0])
        self.assertEqual(nn.layers[1].neurons[0].output > 0.9, True)
        nn.feed_forward2([1, 1])
        self.assertEqual(nn.layers[1].neurons[0].output > 0.9, True)

    def test_and(self):
        nn = NeuralNetwork([])
        nn.createNetwork(2, 1, [2], 1)

        i1 = [0, 0]
        e1 = [0]
        i2 = [1, 0]
        e2 = [0]
        i3 = [0, 1]
        e3 = [0]
        i4 = [1, 1]
        e4 = [1]

        inputs = [i1, i2, i3, i4]
        expected_output = [e1, e2, e3, e4]

        nro_epochs = 4000
        for epoch in range(nro_epochs):
            suma_error = 0
            for i in range(len(inputs)):
                suma_error += nn.train_werror(inputs[i], expected_output[i], 0.5)

        nn.feed_forward2([0, 0])
        self.assertEqual(nn.layers[1].neurons[0].output < 0.1, True)
        nn.feed_forward2([0, 1])
        self.assertEqual(nn.layers[1].neurons[0].output < 0.1, True)
        nn.feed_forward2([1, 0])
        self.assertEqual(nn.layers[1].neurons[0].output < 0.1, True)
        nn.feed_forward2([1, 1])
        self.assertEqual(nn.layers[1].neurons[0].output > 0.9, True)

    def test_nand(self):
        nn = NeuralNetwork([])
        nn.createNetwork(2, 1, [2], 1)

        i1 = [0, 0]
        e1 = [1]
        i2 = [1, 0]
        e2 = [1]
        i3 = [0, 1]
        e3 = [1]
        i4 = [1, 1]
        e4 = [0]

        inputs = [i1, i2, i3, i4]
        expected_output = [e1, e2, e3, e4]

        nro_epochs = 4000
        for epoch in range(nro_epochs):
            suma_error = 0
            for i in range(len(inputs)):
                suma_error += nn.train_werror(inputs[i], expected_output[i], 0.5)


        nn.feed_forward2([0, 0])
        self.assertEqual(nn.layers[1].neurons[0].output> 0.9, True)
        nn.feed_forward2([0, 1])
        self.assertEqual(nn.layers[1].neurons[0].output > 0.9, True)
        nn.feed_forward2([1, 0])
        self.assertEqual(nn.layers[1].neurons[0].output> 0.9, True)
        nn.feed_forward2([1, 1])
        self.assertEqual(nn.layers[1].neurons[0].output < 0.1, True)



if __name__ == '__main__':
    unittest.main()
