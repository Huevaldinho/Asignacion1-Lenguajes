"""
Ejemplos de generadores en python
Creadores
    Garita Granados Alonso - 2021030220
    Sanabria Solano María Fernanda - 2021005572 
    Arguedas Sánchez Raquel Marcela - 2021032567
    Obando Arrieta Felipe de Jesús - 2021035489


Fecha Creación: 20/09/2022
Ultima Modificacion: 20/09/2022
"""

"""
Ejemplo 1 Generador
Fuente: GeeksforGeeks. (2022, 19 septiembre). Python Generators [Software]. https://www.geeksforgeeks.org/generators-in-python/
"""

# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1           
    yield 2           
    yield 3           
  
# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)

"""
Ejemplo 2 Generador
Fuente: GeeksforGeeks. (2022, 19 septiembre). Python Generators [Software]. https://www.geeksforgeeks.org/generators-in-python/
"""

# A Python program to demonstrate use of
# generator object with next()
 
# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
  
# x is a generator object
x = simpleGeneratorFun()
 
# Iterating over the generator object using next
print(next(x)) # In Python 3, __next__()
print(next(x))
print(next(x))