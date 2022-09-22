"""
Creadores
    Garita Granados Alonso - 2021030220
    Sanabria Solano María Fernanda - 2021005572 
    Arguedas Sánchez Raquel Marcela - 2021032567
    Obando Arrieta Felipe de Jesús - 2021035489


Fecha Creación: 20/09/2022
Ultima Modificacion: 20/09/2022
"""

## Corrutinas!
"""
Ejemplo 1 Corrutina
Fuente: EDUCBA. (s. f.). Example of Coroutines python [Software]. https://www.educba.com/coroutines-python/
"""
def bare_bones():
    print("I am writing my primary Coroutine!")
    try:
        while True:
            value = (yield)
            print(value)
    except GeneratorExit:
        print("I am leaving coroutine...")
coroutine = bare_bones()
next(coroutine)
coroutine.send("Hello World!")
coroutine.send("I am learning Coroutines Python")
coroutine.close()


"""
Ejemplo 2 Corrutina
Fuente: GeeksforGeeks. (2022, 6 septiembre). Python Coroutine [Software]. https://www.geeksforgeeks.org/coroutine-in-python/
"""

# Python3 program for demonstrating
# coroutine execution
 
def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)
 
# calling coroutine, nothing will happen
corou = print_name("Dear")
 
# This will start execution of coroutine and
# Prints first line "Searching prefix..."
# and advance execution to the first yield expression
corou.__next__()
 
# sending inputs
corou.send("Atul")
corou.send("Dear Atul")

## Iteradores!
"""
Ejemplo 1 Iteradores
Fuente: w3schools. (s. f.). Example [Software]. https://www.w3schools.com/python/python_iterators.asp
"""
mytuple = ("apple", "banana", "cherry")
# Se itera con la instruccion iter
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


"""
Ejemplo 2 Iteradores
Fuente: w3schools. (s. f.). Example [Software]. https://www.w3schools.com/python/python_iterators.asp
"""
mytuple = ("apple", "banana", "cherry")
# Se itera con la palabra reservada in
for x in mytuple:
  print(x)

## Generador!
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