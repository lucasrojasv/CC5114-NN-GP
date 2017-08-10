from Perceptron import *
import random
from matplotlib import pyplot


a = -2
b = 3
limleft = -50
limright = 50
punto1 = a * limleft + b
punto2 = a * limright + b

nropuntos = 1000
randX = []
randY = []
perceptron = Perceptron([1, 1], 1)
desired_output = []

for i in range(nropuntos):

    randX.append(random.randint(limleft, limright))
    randY.append(random.randint(limleft, limright))

    desired_output.append(0)

    if (a * randX[i] + b) >= randY[i]:
        desired_output[i] = 1

# training phase
training_iterations = 1000
training_error = [1]
suma_error = 0

for j in range(len(randX)):                               ##
    input = [randX[j], randY[j]]
    if perceptron.output(input) != desired_output[i]:  ##
        suma_error += 1  ##3
training_error[0]= (suma_error)/nropuntos

for j in range(1,training_iterations):
    training_error.append(0)                               ##
    suma_error = 0                                          ##
    for i in range(len(randX)):
        input = [randX[i], randY[i]]
        perceptron.train(input, desired_output[i])
        if perceptron.output(input) != desired_output[i]:  ##
            suma_error += 1                                 ##
    training_error[j] = (suma_error)/nropuntos          ##



red_pointsX = []
red_pointsY = []
blue_pointsX = []
blue_pointsY = []
for i in range(len(randX)):
    input = [randX[i], randY[i]]
    if perceptron.output(input) == 0:
        red_pointsX.append(input[0])
        red_pointsY.append(input[1])
    if perceptron.output(input) == 1:
        blue_pointsX.append(input[0])
        blue_pointsY.append(input[1])



#plot all the points
#pyplot.plot(randX,randY)

#plot points red/blue and the lineplot
pyplot.scatter(red_pointsX, red_pointsY, color='r')
pyplot.scatter(blue_pointsX, blue_pointsY, color='b')
pyplot.plot([limleft, limright], [punto1, punto2])

#plot el desempeño
#pyplot.plot(range(training_iterations),training_error)

pyplot.show()
