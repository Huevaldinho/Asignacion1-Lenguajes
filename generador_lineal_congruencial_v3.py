"""
Generador de números pseudoaleatorios
Fuente: Dromey, 'How to solve it by computer'
Algorithm 3.6, 'Generation of pseudo-random numbers'
Adaptado para Python por Ignacio Trejos Zelaya
"""

def siguiente_primo (m):
    ## función no implementada. Por ahora es la identidad.
    return m

def aleatorio (semilla, n):
    ## x tomará como base la semilla
    ## n es la cantidad de números pseudoaleatorios que deseamos generar

    ## Inicializaciones
    ## La literatura  explica la importancia de elegir bien los valores m, a y b
    m = 4096 ## período
    a = 109  ## multiplicador
    b = 853  ## incremento

    ## x será la semilla para iterar (esto puede ser modificado)
    x = siguiente_primo (semilla)

    for i in range (n):
        ## calcular el siguiente número aleatorio
        x = (a * x + b) % m

        ## devolver el siguiente número aleatorio
        yield x

    ## terminar (el for que consuma a este iterador nunca llegará aquí)
    return "fin"

"""
## Descomentar para hacer pruebas
## Semilla, cantidad, rango, frecuencias
semilla = int(input ("Ingrese una semilla, por favor: "))
cuántos = int(input ("¿Cuántos números pseudo-aleatorios desea generar?: "))
rango = int(input ("¿Cuál es el rango de los valores por generar (0 hasta r)?: "))
rango += 1 ## ajuste al rango

##for r in aleatorio (semilla, cuántos):
##    print (r)

lista = [ r for r in aleatorio (semilla, cuántos) ]

en_rango = [ r % rango for r in aleatorio (semilla, cuántos) ]

"""

    
def frecuencias (semilla, n, rango):
    ## Ajuste al rango
    rango += 1 
    ## Crear un vector con n ceros, tantos como para contar frecuencias de los
    ## residuos al dividir un número aleatorio r entre un valor entero (rango)
    frecuencia = [0] * rango

    ## generar números aleatorios y consumirlos iterativamente, contando frecuencias
    for r in aleatorio (semilla, n):
        índice = r % rango
        ## 0 <= índice < rango
        frecuencia[índice] += 1

    print (frecuencia)
    ## es ideal hacer un análisis de 'uniformidad' de los números generados
    ## también es recomendable hacer visualizaciones (como histogramas de frecuencias) en e.g. Matplotlib

    return
    
    
