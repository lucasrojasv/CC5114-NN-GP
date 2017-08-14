from math import exp

class Sigmoid:
################################HACER UNA FUNCION RANDOM , CON SEEDS
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def output(self, input):
        if len(input) != len(self.weights):
            pass

        sum = 0
        for i in range(len(input)):
            sum += self.weights[i]*input[i]

        sigmoid = 1/ (1 + exp(-sum- self.bias))
        return sigmoid

    def train(self, input, desired_output, learning_rate = 0.01):
        c = learning_rate
        epsilon = 0.2
        output = self.output(input)
        if (output > (desired_output + epsilon) ) or ( output < (desired_output - epsilon)) :
            if output < (desired_output - epsilon):
                for i in range(len(self.weights)):
                    self.weights[i] += c*input[i]
            else:
                for i in range(len(self.weights)):
                    self.weights[i] -= c*input[i]
