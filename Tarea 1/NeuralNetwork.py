from NeuronLayer import *
from Neuron import *
import random

# todo: ver si apaña hacer for neuron in layer, o hacer for i in range(len ...

# todo: ver si funciona lo de ir recorriendo un arreglo, si es que los objetos que se recorren son los mmismos
        # todo ver si cambia usando self.layers o usando layers= self.layers


class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers

    #
    # n= new Network()
    # n.setNumberofInput;
    # n.addLayer(2)
    # n.addLayer(1)

    # n.feed({1,0})
    def feed_forward(self, inputs):

        new_inputs = inputs

        for layer in self.layers:
            layer.feed_layer(new_inputs)
            new_inputs = layer.get_outputs()

    def feed_forward2(self, inputs):

        someOutputs = []
        new_inputs = inputs


        # todo ver si cambia usando self.layers o usando layers= self.layers

        for layer_number in range(len(self.layers)):
            someOutputs = []
            current_layer = self.layers[layer_number]

            for neuron_number in range(len(current_layer.neurons)):
                current_neuron = current_layer.neurons[neuron_number]
                current_neuron.feed_neuron(new_inputs)
                someOutputs.append(current_neuron.get_output())
                #for input_number in range(len(new_inputs)):
                #    current_input = new_inputs[inputs]
            new_inputs = someOutputs


    def feed_forward3(self, inputs,expected_output): # return 1 if le achunta

        someOutputs = []
        new_inputs = inputs

        # todo ver si cambia usando self.layers o usando layers= self.layers

        for layer_number in range(len(self.layers)):
            someOutputs = []
            current_layer = self.layers[layer_number]

            for neuron_number in range(len(current_layer.neurons)):
                current_neuron = current_layer.neurons[neuron_number]
                current_neuron.feed_neuron(new_inputs)
                someOutputs.append(current_neuron.get_output())
                #for input_number in range(len(new_inputs)):
                #    current_input = new_inputs[inputs]
            new_inputs = someOutputs


        ##OUTPUT_LAYER
        largo = len(self.layers)
        output_layer = self.layers[largo - 1]
        j=0
        max=0
        k=0
        for i in range(len(output_layer.neurons)):
            valor = output_layer.neurons[i].get_output()
            if (valor >max):
                max = valor
                k = i
            if (expected_output[i] == 1):
                j = i
        m = 0
        if(k == j):
            m=1

        return m


    def error_backpropagation(self, expected_outputs):

        ##OUTPUT_LAYER
        largo = len(self.layers)
        output_layer = self.layers[largo - 1]

        for i in range(len(output_layer.neurons)):                             #/////VER
            neuron=output_layer.neurons[i]
            error = expected_outputs[i] - neuron.get_output()
            neuron.set_delta(error)


        ##HIDEN_LAYERS
        for i in range(largo - 2, -1, -1):
            current_hiddenlayer = self.layers[i]
            next_layer = self.layers[i + 1]
            j = 0  # indice del weight que percibe de las otras neuronas
            for current_neuron in current_hiddenlayer.neurons:                           #/////VER
                sum = 0

                for next_neuron in next_layer.neurons:                                    #/// VER
                    sum += next_neuron.weights[j] * next_neuron.get_delta()  # se pueden optimiziar cosas

                j += 1
                error = sum
                current_neuron.set_delta(error)

    def updating(self, inputs, learning_rate):
        new_inputs = inputs


        for layer in self.layers:

            for neuron in layer.neurons:

                for i in range(len(neuron.weights)):
                    neuron.weights[i] += learning_rate*neuron.get_delta()*new_inputs[i]

                neuron.bias += learning_rate*neuron.get_delta()
                #for weight_num in range(len(neuron.weights)):  ## puedo poner len(inputs) o range(len(neuron.weights

            new_inputs = layer.get_outputs()

    def train_werror(self, input, expected_output, leargning_rate = 0.1):
        self.feed_forward2(input)
        self.error_backpropagation(expected_output)
        self.updating(input,leargning_rate)
        #devuelve mean square

        ##OUTPUT_LAYER
        largo = len(self.layers)
        output_layer = self.layers[largo - 1]
        msq_error = 0
        for i in range(len(output_layer.neurons)):
            msq_error += (output_layer.neurons[i].get_output() - expected_output[i])**2
        return msq_error

    def train(self, input, expected_output, leargning_rate = 0.1):
        self.feed_forward2(input)
        self.error_backpropagation(expected_output)
        self.updating(input,leargning_rate)
        #devuelve mean square


    def createNetwork(self,inputs, nro_hls, hls, outputs):
        assert nro_hls == len(hls)
        network=[]
        network.append(inputs)
        for i in range(nro_hls):
            network.append(hls[i])
        network.append(outputs)

        self.createNeuralNetwork(network)

    #todo Recordar poner una hidden layer almenos.

    def createNeuralNetwork(self,network_vector):
        #usar esto    random.uniform(0, 1)

        # drawnn( [2,8,8,1])
        # 2 Neurons in the input layer
        # 8 Neurons in the 1st hidden layer
        # 8 Neurons in the 2nd hidden layer
        # 1 Neuron in the output layer

        #   [2, 1]
        for i in range(1,len(network_vector)): # al nivel de layer
            nro_weights = network_vector[i-1]
            nro_neurons = network_vector[i]

            layer = []
            for j in range(nro_neurons):       #al nivel de neurona, se crean las neuronas

                weights = []
                for k in range(nro_weights): # se crean el vector weights, para cada neuron

                    weights.append(random.uniform(0, 1))
                bias = random.uniform(0, 1)
                layer.append( Neuron(weights, bias) )  # se añade la neurona al layer

            self.layers.append(NeuronLayer(layer))


















