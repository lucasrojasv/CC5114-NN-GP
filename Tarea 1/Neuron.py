from math import exp
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        self.output = None
        self.delta = None

    def feed_neuron(self, inputk):
#        assert len(input) == len(self.weights)

        sum = 0
        for i in range(len(self.weights)):
            sum += inputk[i]*self.weights[i]

        self.output = 1/ (1 + exp(- sum - self.bias))

    def get_output(self):
        return self.output

    def transfer_derivative(self):
        return self.get_output() * (1 - self.get_output())

    def set_delta(self, error):
        self.delta = error*self.transfer_derivative()

    def get_delta(self):
        return self.delta