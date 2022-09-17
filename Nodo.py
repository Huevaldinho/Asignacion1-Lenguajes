"""
Creadores:


Fecha Creación: 12/09/2022
Ultima Modificacion: 13/09/2022

"""

class Nodo:
    """
        Nodo de un ABB, cada nodo tiene un hijo izquierdo y derecho,
        una llave (identificador) y un valor (contador).
    """
    def __init__(self,llaveIN):
        """
            Crea un nuevo nodo con la llave que recibe.
            Inicializa el valor en 1.

            Parametros:
                -llaveIN int: Numero entero que se le asigna a la llave del nodo
            
            Retorna:
                -No retorna.
        """
        self.hijoIzquierdo = None # Inicializa el hijo izquierdo.
        self.hijoDerecho = None # Inicializa el hijo derecho.
        self.llave = llaveIN #Asigna la llave.
        self.valor = 1 #Inicializa el valor en 1 cuando crea un nodo.

    def obtenerLlave (self):
        """
            Metodo para obtener la llave de un nodo.

            Parametros:
                -Ninguno.
            
            Retorna:
                -self.llave int: Llave del nodo.

        """
        return self.llave

    def obtenerHijoIzquierdo(self):
        """
            Metodo para obtener el hijo izquierdo de un nodo.

            Parametro:
                -Ninguno.
            Retorna:
                -self.hijoIzquierdo Nodo|None: Retorna un Nodo o None. None cuando el hijo izquierdo aun
                no tiene asignado ningun Nodo.

        """
        return self.hijoIzquierdo

    def obtenerHijoDerecho(self):
        """
            Metodo para obtener el hijo derecho de un nodo.

            Parametro:
                -Ninguno.

            Retorna:
                -self.hijoDerecho Nodo|None: Retorna un Nodo o None. None cuando el hijo derecho aun
                no tiene asignado ningun Nodo.

        """

        return self.hijoDerecho

    def asignarHijoIzquierdo(self,hijo):
        """
            Metodo para asignar el hijo izquierdo a un Nodo.

            Parametros:
                -hijo Nodo: Nodo para asignar de hijo izquierdo.
            
            Retorna:
                -No retorna

        """
        self.hijoIzquierdo=hijo

    def asignarHijoDerecho(self,hijo):
        """
            Metodo para asignar el hijo derecho a un Nodo.

            Parametros:
                -hijo Nodo: Nodo para asignar de hijo derecho.
            
            Retorna:
                -No retorna.
        
        """
        self.hijoDerecho=hijo

    def aumentarValor(self):
        """
            Metodo para aumentar en una unidad el valor (contador) del nodo.
            
            Parametros:
                -Ninguno.
            
            Retorna:
                -No retorna.

        """
        self.valor = (self.valor + 1)

    def obtenerValor(self):
        """
            Metodo para obtener el valor (contador) del nodo.

            Parametros:
                -Ninguno.

            Retorna:
                self.valor int: Valor (contador) que tiene el nodo.

        """
        return self.valor