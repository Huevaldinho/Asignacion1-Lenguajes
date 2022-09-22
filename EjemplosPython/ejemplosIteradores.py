"""
Ejemplos de iteradores en python
Creadores
    Garita Granados Alonso - 2021030220
    Sanabria Solano María Fernanda - 2021005572 
    Arguedas Sánchez Raquel Marcela - 2021032567
    Obando Arrieta Felipe de Jesús - 2021035489


Fecha Creación: 20/09/2022
Ultima Modificacion: 20/09/2022
"""

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