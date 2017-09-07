from matplotlib import pyplot
from NeuronLayer import *
from Neuron import *
from NeuralNetwork import *

succeful_rate =[]
nro_epoch = 5000
msq_error = []
for epoch in range(nro_epoch):
    nn = NeuralNetwork([])
    nn.createNetwork(7,2,[8,6],3)                        #cambiar
    suma_error=0

    #train nn epoch times, with the ~80% of the dataset
    for j in range(epoch):
        input_file = open("seed_f_trs.txt",'r')
        for line in input_file:

            array = eval(line)
            suma_error += nn.train_werror(array[0], array[1], 0.1)
        input_file.close()
        print("Despues de mi epoch  / de  " + str(j) + "  " + str(epoch))
    msq_error.append(suma_error)

    #test nn trained "epoch" times, with the ~20% of the dataset
    input_file = open("seed_f_tes.txt", 'r')
    suma_succeful=0
    for line in input_file:

        array = eval(line)
        suma_succeful += nn.feed_forward3(array[0],array[1])
    input_file.close()
    succeful_rate.append( suma_succeful/ 45)


#pyplot.plot(range(nro_epoch),succeful_rate)
pyplot.plot(range(nro_epoch),msq_error)

pyplot.show()