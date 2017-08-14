class Perceptron:
    def __init__(self,weights,bias):
        self.weights = weights
        self.bias = bias



    def output(self,input):
        sum = 0
        for i in range(len(input)):
            sum += input[i]*self.weights[i]

        if (sum + self.bias) > 0:
            return 1
        else:
            return 0

    def train(self,input,desired_output,learning_rate):
        c=learning_rate
        output= self.output(input)
        if output != desired_output:
            if output == 1:
                for i in range(len(self.weights)):
                    self.weights[i] = self.weights[i] - c * input[i]
            else:
                for i in range(len(self.weights)):
                    self.weights[i] = self.weights[i] + c * input[i]






