"""
Ejemplos de corrutinas en python
Creadores
    Garita Granados Alonso - 2021030220
    Sanabria Solano María Fernanda - 2021005572 
    Arguedas Sánchez Raquel Marcela - 2021032567
    Obando Arrieta Felipe de Jesús - 2021035489


Fecha Creación: 20/09/2022
Ultima Modificacion: 20/09/2022
"""

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