from Parser import *


transformar_separar("seed_old.txt","new_seed.txt",3) # 3 clases

minmax = findMaxMin("new_seed.txt") #21.18

normalization("new_seed.txt","seed_f.txt",minmax[0],minmax[1])

desordenar_archivos("seed_f.txt","seed_f_d.txt")