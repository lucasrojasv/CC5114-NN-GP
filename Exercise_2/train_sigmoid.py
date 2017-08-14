from Sigmoid import *
from matplotlib import pyplot
import random

epsilon = 0.5
a = -2
b = 3
limleft = -50
limright = 50
punto1 = a * limleft + b
punto2 = a * limright + b

sigmoid = Sigmoid([1,1],1)

training_iterations = 2000   ########### TO VARY THIS ( no more than 3000 or it freezes)
nropuntos = 1000             ########### TO VARY THIS

suma_error = 0
succeful_rate = []

#training phase
for i in range(training_iterations):
    sigmoid = Sigmoid([1,1],1)
    suma_error = 0

    # train sigmoid i times with random points
    for j in range(i):
        randomX = random.uniform(limleft,limright)
        randomY = random.uniform(limleft,limright)
        desired_output = 0

        if (a*randomX + b) >= randomY:
            desired_output = 1

        input = [randomX, randomY]
        sigmoid.train(input, desired_output)

    #test trained sigmoid in "nropuntos" time with random points
    for k in range(nropuntos):
        randomX = random.uniform(limleft,limright)
        randomY = random.uniform(limleft,limright)
        desired_output = 0
        if (a * randomX + b) >= randomY:
            desired_output = 1

        input = [randomX, randomY]
        if (sigmoid.output(input) > (desired_output + epsilon)) or (sigmoid.output(input) < desired_output - epsilon ):
            suma_error += 1

    succeful_rate.append( (nropuntos- suma_error) / nropuntos)



##plot de los puntos
randX = []
randY = []
red_pointsX = []
red_pointsY = []
blue_pointsX = []
blue_pointsY = []

for i in range(nropuntos):
    randX.append(random.uniform(limleft, limright))
    randY.append(random.uniform(limleft, limright))

    input = [randX[i], randY[i]]
    if sigmoid.output(input) >= 0.5:
        red_pointsX.append(input[0])
        red_pointsY.append(input[1])
    else:
        blue_pointsX.append(input[0])
        blue_pointsY.append(input[1])

##plot points red/blue and the lineplot    with random points
#pyplot.scatter(red_pointsX, red_pointsY, color='r')
#pyplot.scatter(blue_pointsX, blue_pointsY, color='b')
#pyplot.plot([limleft, limright], [punto1, punto2])

############################################################# UNCOMMENT TO PLOT WHAT YOU WANT

##plot del desempeño
pyplot.plot(range(training_iterations),succeful_rate)

pyplot.show()