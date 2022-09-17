"""
Creadores

Fecha Creación: 11/09/2022
Ultima Modificacion: 13/09/2022

Fuente del metodo buscarNodo: Salcedo, L. (19/07/2018). Árbol binario de búsqueda - Estructura de datos en Python.
                            Mi Diario Python. Consultado el 12 de Septiembre de 2022.
                            https://pythondiario.com/2018/07/arbol-binario-de-busqueda-estructura-de.html.
Modificado por Felipe Obando Arrieta para que retorne True|False.


"""


from Nodo import Nodo

class ABB:
    """
            La clase ABB (Árbol Binario de Búsqueda) contieneun nodo raíz,
        cada nodo tiene un hijo derecho e hijo izquierdo,
        junto con dos numeros enteros: llave (identificador) y valor (contador).
    """
    def __init__(self):
        """
            El método constructor __init__ instancia el árbol, inicializa la raiz en None.

        Parameteros:
            -Ninguno.
        Retorna:
            -No retorna.
        
        """
        self.raiz = None # Inicializa el nodo raiz del árbol en None.

    ##Funciones solicitadas en el proyecto        
    ##-------------------------------------------------#
    def insertar(self,llaveIN):
        """
            Metodo para insertar una llave en el arbol.

        Si la llave no se encuentra en el árbol, crea un nuevo nodo con la llave e inicializa el contador en 1. 
        Si la llave ya se encuentra en el árbol, no la inserta, pero suma 1 al contador asociado con esa llave (en el nodo).

        Parametros
            -llaveIn: numero entero para asignar a la llave del nodo.
        Retorna:
            -No retorna.

        """
        if (self.buscarNodo(llaveIN)): #La llave ya se encuentra en el arbol.
            #Obtiene el nodo con la llaveIN.
            nodoLlaveBuscada = self.obtenerNodo(llaveIN,self.obtenerRaiz())
            nodoLlaveBuscada.aumentarValor() #Aumenta el contador+1  del nodo con la llaveIN.
           
        else: #No existe el nodo con la llaveIN.
            nodoActual = None
            if (self.esVacia()): #Si el arbol esta vacio
                self.raiz = nodoActual = Nodo(llaveIN) #Le crea el nodo en la raiz.
                 
            else: #El arbol no esta vacio

                nodoActual = nodoPadre = self.obtenerRaiz() #Toma la raiz para empezar a buscar donde insertarlo

                #Mientras el nodo actual no sea una hoja, se ejecuta el ciclo.
                while nodoActual is not None: 
                    nodoPadre = nodoActual #Guarda el ultimo nodo para poder enlazarlo con el nuevo
                    if (llaveIN <= nodoActual.obtenerLlave()): #La llave es menor o igual que el nodo
                        nodoActual = nodoActual.obtenerHijoIzquierdo()
                    else:
                        nodoActual = nodoActual.obtenerHijoDerecho()

                #Cuando se sale del ciclo es porque ya llego a una hoja donde puede insertar el nuevo nodo
                nodoActual = Nodo(llaveIN)
                #Si el nodoPadre es mayor que el nodo actual, el actual sera el hijo izquierdo del padre
                if (nodoPadre.obtenerLlave() > nodoActual.obtenerLlave()):
                    nodoPadre.asignarHijoIzquierdo(nodoActual)
                else:
                    nodoPadre.asignarHijoDerecho(nodoActual)
            print("Se ha insertado nodo con la llave: ",nodoActual.obtenerLlave())


    def buscarNodo(self,llaveBuscada):
        """
            Metodo para buscar el nodo con la llaveBuscada en el arbol.

            Fuente: Salcedo, L. (19/07/2018). Árbol binario de búsqueda - Estructura de datos en Python.
            Mi Diario Python. Consultado el 12 de Septiembre de 2022.
            https://pythondiario.com/2018/07/arbol-binario-de-busqueda-estructura-de.html.
            

            Modificado por Felipe Obando Arrieta para que retorne True| False, en lugar de None|Nodo.

            Metodo para la búsqueda de un valor entero (la llave) en el ABB sin hacer inserciones. 
            La función debe retornar un valor booleano que indique si encontró la llave buscada (true = la encontró, false = no la encontró).

        Parametros:
            -llaveBuscada int: Numero entero que se busca encontrar en las llaves de los nodos del arbol.
        
        Retorna:
            -True|False bool: Retorna verdadero si encontro la llaveBuscada, False si NO la encontro.
        """
        nodoActual = None #Variable para buscar en el arbol el nodo con la llaveBuscada.
        if (self.esVacia()): #Si el arbol esta vacio, la llave no puede estar en el.
            return False
        else: #El arbol no esta vacio, se debe buscar entre sus nodos.
            nodoActual = self.obtenerRaiz() #Se empieza a buscar la llave desde la raiz del arbol.

            #Se utiliza un while porque no se sabe cuantos elementos tiene el arbol
            
            #Mientras el nodoActual no sea una hoja y la llave del nodo no sea la buscada, continua el ciclo.
            while nodoActual is not None and nodoActual.obtenerLlave() is not llaveBuscada:

                #Si entra al ciclo es porque aun no llega a una hoja y no encuentra la llave buscada
                if (llaveBuscada < nodoActual.obtenerLlave()): #Si la llaveBuscada es menor que el nodo actual, busque en los menores
                    nodoActual = nodoActual.obtenerHijoIzquierdo() #Cambia al hijo izquierdo del nodo actual (menor).
                else: #Si la llaveBuscada es mayor a la del nodo actual.
                    nodoActual = nodoActual.obtenerHijoDerecho() #Cambia al hijo derecho del nodo actual (mayor).

                #El while no se encicla porque esta bajando por una rama, entonces que en algun momento
                #lega a una hoja o al nodo con la llave buscada.

        #Termino de buscar la llave en el arbol
        if nodoActual is not None: #Si el nodoActual no es None significa que si encontro el nodo con la lleveBuscada.
            return True
        return False 

    def obtenerNodo(self,llaveBuscada,nodoActual):
        """
            Metodo para obtener el nodo con la llaveBuscada.

        Parametros:
            -llaveBuscada int: Numero entero que se busca encontrar en las llaves de los nodos del arbol.
            -nodoActual Nodo|None: Nodo donde se buscara la llave o se baja a buscar en sus hijos.
        
        Retorna:
            -Nodo|none: Retorna el nodo con la llaveBuscada o None si no la encuentra.
        """
        if (nodoActual == None): #Si el nodoActual es None es porque el arbol esta vacio o porque
                                #en la recursion de otra llamada se llego a una hoja
            return False
        else: #El nodo actual tiene llave para buscar o en sus hijos
            llaveNodoActual = nodoActual.obtenerLlave() #Saca la llave del nodo actual
            if llaveNodoActual == llaveBuscada: #La llave del nodo actual es la buscada
                return nodoActual #Retorna el nodo actual
            elif llaveNodoActual > llaveBuscada: #La llaveBuscada es menor que la actual
                return self.obtenerNodo(llaveBuscada,nodoActual.obtenerHijoIzquierdo()) #Continua la busqueda en los menores
            else: #La llaveBuscada es mayor que la actual
                return self.obtenerNodo(llaveBuscada,nodoActual.obtenerHijoDerecho()) #Continua la busqueda en los mayores

    ##-------------------------------------------------#


    ##Funciones basicas para utilizar arboles
    ##-------------------------------------------------#
    def esVacia(self):
        """
            Determina si el arbol esta vacio.

        Parametros: 
            -Ninguno.
        
        Returna:
            -True|False bool: Verdadero si la lista esta vacia, falso si la lista NO esta vacia.
        """
        if self.raiz is None:
            return True
        return False

    def obtenerRaiz(self):
        """
            Metodo para obtener la raiz del arbol

        Parametros:
            -Ninguno.
        
        Retorna:
            -self.raiz Nodo|None: Retorna el nodo raiz del arbol. None el arbol no tiene nodos.
        """
        return self.raiz
    ##-------------------------------------------------#

    ##Recorridos del arbol
    #Cada uno de ellos debe entregar un par (llave, contador)
    ##-------------------------------------------------#
    def enorden(self,nodoActual):
        """
            Metodo para recorrer el arbol en inorden. izquierda - raiz - derecha

        Parametros:
            -nodoActual Nodo: Nodo para realizar recorrido.

        Retorna:
            -No retorna.
            
        """
        if nodoActual is not None:
            self.enorden(nodoActual.obtenerHijoIzquierdo()) #Recorre todo por la izquierda
            print((nodoActual.obtenerLlave(),nodoActual.obtenerValor())) #Cuando termina de recorrer todo izquierda imprime centro
            self.enorden(nodoActual.obtenerHijoDerecho()) #Recorre todo por derecha

    def generadorEnOrden(self,nodoActual):
        """
            Metodo para generar recorrido del arbol enOrden.
                izquierda - raiz - derecha

        Parametros:
            -nodoActual Nodo|None: Recibe un nodo del arbol o None si es una hoja del arbol.
        
        Retorna: 
            -(llave,valor) (int,int): Tupla de enteros.

        """
        if nodoActual is not None: #Mismo funcionamiento que un enOrden pero
            #yield from toma todos los resultados de la llamada recursiva
            yield from self.generadorEnOrden(nodoActual.obtenerHijoIzquierdo())
            #yield toma llave:valor
            yield (nodoActual.obtenerLlave(),nodoActual.obtenerValor())
            yield from self.generadorEnOrden(nodoActual.obtenerHijoDerecho())
          
       
       
    def generarPreOrden(self,nodoActual):
        """
            Metodo para generar recorrido del arbol en preOrden.
                raiz - izquierda - derecha

        Parametros:
            -nodoActual Nodo: Nodo para realizar recorrido.

        Retorna:
            -No retorna.

        """
        if nodoActual is not None:
            #print("Llave:",nodoActual.obtenerLlave()," | Valor:",nodoActual.obtenerValor())
            yield (nodoActual.obtenerLlave(),nodoActual.obtenerValor())
            yield from self.generarPreOrden(nodoActual.obtenerHijoIzquierdo())
            yield from self.generarPreOrden(nodoActual.obtenerHijoDerecho())

    def generarPostOrden(self,nodoActual):
        """
            Metodo para generar recorrido del arbol en postOrden. 
                izquierda - derecha - raiz

        Parametros:
            -nodoActual Nodo: Nodo para realizar recorrido.

        Retorna:
            -No retorna.
            
        """
        if nodoActual is not None:
            yield from self.generarPostOrden(nodoActual.obtenerHijoIzquierdo())
            yield from self.generarPostOrden(nodoActual.obtenerHijoDerecho())
            yield (nodoActual.obtenerLlave(),nodoActual.obtenerValor())
            
    ##-------------------------------------------------#

arbol = ABB()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(8)
arbol.insertar(12)
arbol.insertar(17)#1
print()
#arbol.enorden(arbol.obtenerRaiz())
arbol.insertar(17)#2
arbol.insertar(17)#3
arbol.insertar(17)#4

#arbol.enorden(arbol.obtenerRaiz())

#Crea el generador en orden del arbol
generadorEnOrden = arbol.generadorEnOrden(arbol.obtenerRaiz())
#Toma el menor elemento del arbol
#print(next(generadorEnOrden))
#print(next(generadorEnOrden))
#print(next(generadorEnOrden))
#print(next(generadorEnOrden))

print("Recorrer generador en orden")
for i in generadorEnOrden:#range(1,5):
    #print(next(generadorEnOrden))
    print(i)

print("Recorrer generador en postOrden")
generadorPostOrden = arbol.generarPostOrden(arbol.obtenerRaiz())
for j in generadorPostOrden:
    print(j)