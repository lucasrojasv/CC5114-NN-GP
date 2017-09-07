from matplotlib import pyplot
from NeuronLayer import *
from Neuron import *
from NeuralNetwork import *

nro_epochs = 5000
nn = NeuralNetwork([])
nn.createNetwork(7,1,[8],3)
msq_error = []
succeful_rate = []

for epoch in range(nro_epochs):
    input_file = open("seed_f_trs.txt", 'r')
    suma_error = 0

    # train nn with the ~20% of the dataset
    for line in input_file:
        array = eval(line)
        suma_error += nn.train_werror(array[0], array[1], 0.1) #usar 0.05
        #nn.train(array[0], array[1], 0.3)  # usar 0.05
    input_file.close()
    print("Despues de mi epoch nro:   " + str(epoch))
    msq_error.append(suma_error)


    input_file = open("seed_f_tes.txt", 'r')

    # test nn with the ~20% of the dataset
    suma_succeful = 0
    for line in input_file:

        array = eval(line)
        suma_succeful += nn.feed_forward3(array[0], array[1])
    succeful_rate.append(suma_succeful/45)
    input_file.close()


#pyplot.plot(range(nro_epochs),msq_error)
pyplot.plot(range(nro_epochs),succeful_rate)

pyplot.show()