"""
Generador de números primos
Fuente: Creación propia
Autor: Alonso Garita Granados
"""

def generarPrimos(n):
    """
    Params:
        n: Cantidad de primos para generar
    Yield:
        m: Candidato validado como primo en secuencia
    Return:
        None
    """
    
    isPrimo = True #Asumimos que el número es primo
    primos = []
    i = 0 #Contador para generar n primos
    m = 2 #Candidatos a primos iniciando desde 2

    while (i < n):
        for p in primos:
            if(m % p == 0): #Chequea si es divisible entre otro primo averiguado
                isPrimo = False
                break

        if(isPrimo): #Si es primo:
            primos.append(m) #Lo agrega
            yield m #Lo libera
            i+=1 #Incrementa el contador
        else: #Sino
            isPrimo = True #Asumimos el siguiente como primo
        m+=1 #Siguiente candidato

    return None

def test():

    for p in generarPrimos(1000):
        q = p + 2
        if(q in generarPrimos(1000)):
            #Si q es igual a algún valor generado por generarPrimos...
            print("(", p, ",", q, ")", end=" , ")

    return None

##test()

