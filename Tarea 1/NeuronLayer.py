from Neuron import *
class NeuronLayer:
    def __init__(self, neurons):
        self.neurons = neurons

    def feed_layer(self, inputs):

        for neuron in self.neurons:
            neuron.feed_neuron(inputs)

    def get_outputs(self):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.get_output())

        return outputs
