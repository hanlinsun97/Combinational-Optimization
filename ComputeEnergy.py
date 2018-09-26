import numpy as np
import random

#  N: Number of Queens
#  seq: Order (Position) of Queens 
#  


def ComputeEnergy(N, seq):
    
    #  Coordinate Tuple
    X = list(range(N))
    Y = seq
    coordinate = zip(X, Y)
    coordinate = list(coordinate)
    Energy = 0
    for i in range(N):
        for j in range(N):
            if j != i:
                if abs(coordinate[j][1] - coordinate[i][1]) == abs(coordinate[j][0] - coordinate[i][0]):
                    Energy += 1
    return Energy, coordinate

N = 15
for i in range(1000000):
    seq = list(range(N))
    random.shuffle(seq)
  
    Energy, coordinate = ComputeEnergy(N, seq)
    if Energy == 0:
        print(Energy)
        print(coordinate)
  