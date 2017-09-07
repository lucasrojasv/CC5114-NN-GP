import random

def desordenar_archivos(nombre_archivo1,nombre_archivo2):
    array_lineas =[]
    input_file = open(nombre_archivo1,'r')
    output_file = open(nombre_archivo2, 'w')
    for line in input_file:
        array_lineas.append(eval(line))
    random.shuffle(array_lineas)
    for i in range(len(array_lineas)):
        output_file.write(str(array_lineas[i])+"\n")
    input_file.close()
    output_file.close()

def normalizar(x, d_h,d_l,n_h,n_l):
    return (x - d_l) * (n_h - n_l) / (d_h - d_l) + n_l


def testeo_files(nombre_archivo):
    infile = open(nombre_archivo,'r')
    for line in infile:
        array =eval(line)
        nuevo_input = []
        for element in array[0]:
            print(element)

    infile.close()

def normalization(nombre_archivo1,nombre_archivo2,maximo,low):
    infile = open(nombre_archivo1,'r')
    output = open(nombre_archivo2,'w')

    for line in infile:
        array =eval(line)
        nuevo_input = []
        nuevo_array =[]
        for element in array[0]:
            x = normalizar(element,maximo,low,1,0)
            nuevo_input.append(x)
        nuevo_array.append(nuevo_input)
        nuevo_array.append(array[1])
        output.write(str(nuevo_array)+"\n")

    infile.close()
    output.close()

def findMaxMin(nombre_archivo):                                          #2 !!!!!!!
    infile = open(nombre_archivo,'r')
    max=0
    min=0
    for line in infile:
        array =eval(line)
        for element in array[0]:
            if(element>max):
                max = element
            elif(element < min):
                min = element
    infile.close()
    print([max,min])




def transformar_separararray(nombre_archivo1,nombre_archivo2,nro_clases): #eval( )     #1  !!!!!!!1
    infile =open(nombre_archivo1,'r')
    output = open(nombre_archivo2,'w')
    nuevo_array = []
    for line in infile:
        nuevo_array =[]
        array = line.split(',')
        #array = list(map(int,array))
        print(array)
        print(array[0])
        nro_letra = cambiarLetraporNumero(array[0])
        print(nro_letra)
        nuevo_input=[]
        nuevo_expectedoutput=[]                            ##

        ###### esto es para poner el vector de inputs
        for i in range(1,len(array)):
            nuevo_input.append(eval(array[i]))

        nuevo_array.append(nuevo_input)

        ##### esto es para poner el vector de expected outputs de la forma [1,0,0,..,0]
        for i in range(nro_clases):
            if(i==(nro_letra-1)):
                nuevo_expectedoutput.append(1)
            else:
                nuevo_expectedoutput.append(0)
        nuevo_array.append(nuevo_expectedoutput)



        #nuevo_array.append(nro_letra)
        output.write(str(nuevo_array)+"\n")

        #print(Letras.eval(array[0]))
    output.close()
    infile.close()
# from enum import Enum

def transformar_separar(nombre_archivo1,nombre_archivo2,nro_clases): #eval( )     #1  !!!!!!!1
    infile =open(nombre_archivo1,'r')
    output = open(nombre_archivo2,'w')
    nuevo_array = []
    for line in infile:
        nuevo_array =[]
        print(line)
        #array = line.split(',')
        array = line.split(',')
        #array = list(map(int,array))

        #print(array[len(array)-1])
        #print(array[len(array)-2])
        #nro_letra = cambiarLetraporNumero(array[0])
        nro_clase = array[len(array)-1]
        #print(nro_clase)
        #print(array[len(array)-1])
        #print(array[len(array) - 2])
        #print(array[len(array) - 3])



        nro_clase = eval(nro_clase  )
        #print(nro_clase)

        #print(nro_letra)
        nuevo_input=[]
        nuevo_expectedoutput=[]                            ##

        ###### esto es para poner el vector de inputs
        for i in range(len(array)-1):
            nuevo_input.append(eval(array[i]))
            print(eval(array[i]))
        nuevo_array.append(nuevo_input)

        ##### esto es para poner el vector de expected outputs de la forma [1,0,0,..,0]
        for i in range(nro_clases):
            if(i==(nro_clase-1)):
                nuevo_expectedoutput.append(1)
            else:
                nuevo_expectedoutput.append(0)
        nuevo_array.append(nuevo_expectedoutput)



        #nuevo_array.append(nro_letra)
        output.write(str(nuevo_array)+"\n")

        #print(Letras.eval(array[0]))
    output.close()
    infile.close()