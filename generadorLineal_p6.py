"""
Generador de números pseudoaleatorios
Fuente: Dromey, 'How to solve it by computer'
Algorithm 3.6, 'Generation of pseudo-random numbers'
Adaptado para Python por Ignacio Trejos Zelaya
Modificado por Alonso Garita Granados
"""

def aleatorio (semilla, n):
    """
    Params:
        semilla: número a partir del que se define el primer número pseudoaleatorio
        n: cantidad de números pseudoaleatorios deseados
    Yield:
        x: i-ésimo número pseudoaleatorio de la sucesión
    Return:
        None
    """

    #Si la semiila es menor que 11, forzamos a que sea 11
    if(semilla < 11):
        semilla = 11

    # Inicializaciones
    # Parámetros tomados de la implementación de Dromey (1982)
    m = 4096 ## Periodo
    a = 109  ## Multiplicador
    b = 853  ## Incremento

    #Definir el primer número pseudoaleatorio (x0)
    x = 0
    isPrimo = True
    primos = [2, 3, 5, 7] # No hace falta validar valores menores que 11
    repeat = True
    candidato = 11 # Interesa buscar primos mayores o iguales que 11

    #Verifica para todos los enteros entre 11 y x0 cuál es el primo para definir x0
    #Fuente: Item 5 del presente trabajo
    while (repeat):
        for p in primos:
            if(candidato % p == 0):
                isPrimo = False
                break

        if(isPrimo):
            if(candidato >= semilla):
                x = candidato
                repeat = False
        else:
            isPrimo = True
        candidato+=1

    #En este punto, con certeza x es primo y x >= semilla

    for i in range(n):
        #Liberar el número pseudoaleatorio actual
        yield x
        #Calcular el siguiente número pseudoaleatorio
        x = (a * x + b) % m

    #Nunca se llega a este return
    return None


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
