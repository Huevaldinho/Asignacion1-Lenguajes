"""
Generador de números pseudoaleatorios
Fuente: Dromey, 'How to solve it by computer'
Algorithm 3.6, 'Generation of pseudo-random numbers'
Adaptado para Python por Ignacio Trejos Zelaya
Modificado por Alonso Garita Granados
"""

import generadorPrimos as gp

def aleatorio (semilla, n):
    ## x tomará como base la semilla
    ## n es la cantidad de números pseudoaleatorios que deseamos generar

    if(semilla < 11): #Se asegura que la semilla sea al menos 11
        semilla = 11

    ## Inicializaciones
    ## La literatura  explica la importancia de elegir bien los valores m, a y b
    m = 4096 ## período
    a = 109  ## multiplicador
    b = 853  ## incremento

    #--Seleccionar el x primo a partir del cual generar los aleatorios
    x = 0
    isPrimo = True
    primos = [2, 3, 5, 7] # No hace falta validar valores menores que 11
    repeat = True
    m = 11 # Interesa buscar primos mayores o iguales que 11

    while (repeat):
        for p in primos:
            if(m % p == 0):
                isPrimo = False
                break

        if(isPrimo):
            if(m >= semilla):
                x = m
                repeat = False
        else:
            isPrimo = True
        m+=1

    #--Cuando sale, con certeza x >= semilla

    for i in range (n):
        ## devolver el número aleatorio actual
        yield x
        ## calcular el siguiente número aleatorio
        x = (a * x + b) % m

    ## terminar (el for que consuma a este iterador nunca llegará aquí)
    return "fin"

## Semilla, cantidad, rango, frecuencias
semilla = int(input ("Ingrese una semilla, por favor: "))
cuántos = int(input ("¿Cuántos números pseudo-aleatorios desea generar?: "))
rango = int(input ("¿Cuál es el rango de los valores por generar (0 hasta r)?: "))
rango += 1 ## ajuste al rango

lista = [ r for r in aleatorio (semilla, cuántos) ]

for r in lista:
        print (r)

en_rango = [ r % rango for r in aleatorio (semilla, cuántos) ]

for r in en_rango:
        print (r)

