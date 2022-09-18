import generadorLineal_p6 as genRand
#import ABB

def generarHistograma(xABB):
    #Lo que hizo Fer
    return None

def llenarABB(xABB):
    """
    Params:
        pABB: El árbol o lo que ocupe enviar para llenarlo
    Return:
        None, o lo que ocupe retornar
    """

    for n in [300, 600, 900, 1200]: #Para probar se pueden reducir los valores de n
        print("n = ", n)
        for semilla in [20, 50, 100, 200]:
            print("semilla = ", semilla)
            for r in genRand.aleatorio(semilla, n):
                print("rand: ", r) #Aquí se inserta r en el ABB
            
            generarHistograma(xABB) #Aquí se tiene el ABB lleno y se puede graficar con lo que hizo Fer
            #xABB.vaciar() #También se debería vaciar el ABB

            
    return None

llenarABB(None)