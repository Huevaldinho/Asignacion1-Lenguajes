"""
Creadores
    Garita Granados Alonso - 2021030220
    Sanabria Solano María Fernanda - 2021005572 
    Arguedas Sánchez Raquel Marcela - 2021032567
    Obando Arrieta Felipe de Jesús - 2021035489

Fecha Creación: 17/09/2022
Ultima Modificacion: 19/09/2022
"""
import matplotlib.pyplot as plt
import math
import ABB as treeABB
def getBins(n, maxi, mini):
    """
        Calcular intervalor de clases segun la muestra, el minimo y el maximo

        Parametros:
            -n (int): Cantidad de muestras.
            -maxi (int): Valor maximo
            -mini (int): Valor minimo

        Retorna:
            list: Intervalos de clase.
    """
    span = maxi-mini
    width = int( span / (math.sqrt(n)))
    intervals = []
    for i in range(mini, span+width, width+1):
        intervals.append(i)
    intervals.append(span+width)
    return intervals

def getData(tree):
    """
        Retorna una lista con los datos ordenados del arbol tree

        Parametros:
            -tree (ABB): Arvol binario de busqueda donde se agarran los datos

        Retorna:
            list: Lista con datos ordenados
    """
    generadorEnOrden = tree.generadorEnOrden(tree.obtenerRaiz())
    datos = []
    for i in generadorEnOrden:#range(1,5):
        for j in range(0,i[1]):
            datos.append(i[0])
    return datos
    
def createHistogram(x):
    """
        Muestra un histograma con los datos de x

        Parametros:
            -x (list): Lista de datos

        Retorna:
            
    """
    plt.hist(x, bins=getBins(len(x), x[-1], x[0]))
    plt.xlabel("Número")
    plt.ylabel("Repeticiones")
    plt.show()



def main():
    arbol = treeABB.ABB()
    arbol.insertar(10)
    arbol.insertar(5)
    arbol.insertar(15)
    arbol.insertar(3)
    arbol.insertar(8)
    arbol.insertar(12)
    arbol.insertar(17)
    arbol.insertar(17)
    arbol.insertar(17)
    arbol.insertar(17)    
    createHistogram(getData(arbol))

# main()

# histogram([17, 20, 22, 25, 26, 27, 30, 31, 32, 38, 40, 40, 45, 55])

# Para descargar la libreria matplotlib
# C:\Users\mfss0>cd\
# C:\>cd C:\Users\mfss0\AppData\Local\Programs\Python\Python39\Scripts
# C:\Users\mfss0\AppData\Local\Programs\Python\Python39\Scripts>pip install matplotlib