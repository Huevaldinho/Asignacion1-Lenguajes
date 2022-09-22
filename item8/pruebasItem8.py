"""
Creadores
    Garita Granados Alonso - 2021030220
    Sanabria Solano María Fernanda - 2021005572 
    Arguedas Sánchez Raquel Marcela - 2021032567
    Obando Arrieta Felipe de Jesús - 2021035489

Fecha Creación: 19/09/2022
Ultima Modificacion: 20/09/2022
"""

import generadorLineal_p6 as genRand
import histograma as hist
import ABB as tree

def llenarABB(xABB):
    """
    Parametross:
        xABB: El árbol o lo que ocupe enviar para llenarlo
    Return:
        None, o lo que ocupe retornar
    """

    for n in [300, 600, 900, 1200]: #Para probar se pueden reducir los valores de n
        print("n = ", n)
        for semilla in [20, 50, 100, 200]:
            print("semilla = ", semilla)
            for r in genRand.aleatorio(semilla, n):
                # print("rand: ", r, " Numero a insertar: ", r%100) #Aquí se inserta r%100 en el ABB
                xABB.insertar(r%100)
            hist.createHistogram(hist.getData(xABB))
           
            xABB.reiniciarRaiz() #También se debería vaciar el ABB

            
    return None

llenarABB(tree.ABB())