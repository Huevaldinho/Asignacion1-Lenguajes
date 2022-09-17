# Fecha Creacion: 17/09/2022
# Ultima Modificacion: 16/09/2022

import matplotlib.pyplot as plt
import math
def getBins(n, maxi, mini):
    span = maxi-mini
    width = int( span / (math.sqrt(n)))
    intervals = []
    for i in range(mini, span+width, width+1):
        intervals.append(i)
    intervals.append(span+width)
    return intervals

def histogram(x):
    plt.hist(x, bins=getBins(len(x), x[-1], x[0]))
    plt.xlabel("Número")
    plt.ylabel("Repeticiones")
    plt.show()

histogram([17, 20, 22, 25, 26, 27, 30, 31, 32, 38, 40, 40, 45, 55])