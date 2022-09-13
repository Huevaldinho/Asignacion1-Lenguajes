#Creadores
#Fecha Creación 11/09/2022
#Referencia para el buscar iterativo: Luis Salcedo (19/07/2018 - Actualizado: 22/12/2020)
# https://pythondiario.com/2018/07/arbol-binario-de-busqueda-estructura-de.html

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
                No retorna.
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
        self.hijoIzquierdo=hijo
    def asignarHijoDerecho(self,hijo):
        self.hijoDerecho=hijo
    def aumentarValor(self):
        """
            Suma uno al valor (contador) del nodo.
            
            Parametros:
                Ninguno.
            
            Retorna:
                No retorna.

        """
        self.valor = (self.valor + 1)
    def obtenerValor(self):
        return self.valor
    
class ABB:
    """
            La clase ABB (Árbol Binario de Búsqueda) contiene
        un nodo raíz, cada nodo tiene un hijo derecho e hijo izquierdo,
        junto con dos numeros enteros: llave (identificador) y valor (contador).
    """
    def __init__(self):
        """
            El método constructor __init__ instancia el árbol, inicializa la raiz en None.

        Parameteros:
            Ninguno.
        Retorna:
            No retorna.
        
        """
        self.raiz = None # Inicializa el nodo raiz del árbol en None.

    ##Funciones solicitadas en el proyecto        
    ##-------------------------------------------------#
    def insertar(self,llaveIN):
        """
            Una función que haga la inserción de un valor entero (la llave) en el ABB. 

            Si la llave no se encuentra en el árbol, crea un nuevo nodo con la llave e inicializa el contador en 1. 
            Si la llave ya se encuentra en el árbol, no la inserta, pero suma 1 al contador asociado con esa llave (en el nodo).

            Parametros
                -llaveIn: numero entero para asignar a la llave del nodo.
            Retorna:
                No retorna.

        """
        if (self.buscarNodo(llaveIN)): #La llave ya se encuentra en el arbol.
            #Obtiene el nodo (o None) con la llaveIN, le pasa la raiz del arbol para que empiece a buscar el nodo.
            nodoLlaveBuscada = self.obtenerNodo(llaveIN,self.obtenerRaiz())
            if (nodoLlaveBuscada is not None): #Si no es None es porque si obtuvo el nodo con la llaveIN.
                nodoLlaveBuscada.aumentarValor() #Aumenta el contador+1  del nodo con la llaveIN.
            else: #En teoria no debe llegar aqui porque buscar nodo me confirma que el nodo con la llaveIN si existe.
                print("No existe nodo con la llave:",llaveIN)
        else: #No existe el nodo con la llaveIN.
            nodoActual = None
            if (self.esVacia()): #Si el arbol esta vacio
                self.raiz = nodoActual = Nodo(llaveIN) #Le crea el nodo en la raiz.
                 
            else: #El arbol no esta vacio

                nodoActual = nodoPadre = self.obtenerRaiz() #Toma la raiz para empezar a buscar donde insertarlo
                 
                while nodoActual is not None: #Mientras el nodo actual no sea una hoja, se ejecuta el ciclo.
                    nodoPadre = nodoActual
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
            PREGUNTARLE AL PROFE SI SE PUEDE MODIFICAR LOS VALORES QUE RETORNA
            A None para cuando no existe en el arbol o el Nodo que contiene la llave.

            Como solo se puede tener un parametro (llaveBuscada), no se puede utilizar recursion
            para ir bajando en el arbol a traves de los nodos hijos. Se tiene que hacer
            iterativo.

            Una función que haga la búsqueda de un valor entero (la llave) en el ABB sin hacer inserciones. 
            La función debe retornar un valor booleano que indique si encontró la llave buscada (true = la encontró, false = no la encontró).

            Parametros:
                -llaveBuscada int: Numero entero que se busca encontrar en las llaves de los nodos del arbol.
            
            Retorna:
                -True bool: Retorna verdadero si encontro la llaveBuscada en el arbol.
                -False bool: Retorna falso si no encontro la lleveBuscad en el arbol.
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
        return False #Si None es porque llevo a una hoja, por lo tanto NO encontro la llave buscada.

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
    ##-------------------------------------------------#
    def preorder(self,nodoActual):
        """Descripción de la función
        Parameters
        ----------
        parametro_1 : tipo
            Descripción del parametro
        parametro_2 : tipo
            Descripción del parametro
        Returns
        -------
        tipo
            Descripción de los valores que devuelve
        """
        ##Recorre el arbol node en sentido raiz - hijo izquierdo - hijo derecho.
        ## node Node: Recibe un objeto de tipo Node.
        ##Cuando la recursion llega a una hoja no entra en el if node
        ##entonces la recursion se regresa para continuar con el recorrido.
        
        if nodoActual is not None:
            print("Llave:",nodoActual.obtenerLlave()," | Valor:",nodoActual.obtenerValor())
            self.preorder(nodoActual.obtenerHijoIzquierdo())
            self.preorder(nodoActual.obtenerHijoDerecho())

    def inorder(self,nodoActual):
        """Descripción de la función
        Parameters
        ----------
        parametro_1 : tipo
            Descripción del parametro
        parametro_2 : tipo
            Descripción del parametro
        Returns
        -------
        tipo
            Descripción de los valores que devuelve
        """
        if nodoActual is not None:
            self.inorder(nodoActual.obtenerHijoIzquierdo())
            print("Llave:",nodoActual.obtenerLlave()," | Valor:",nodoActual.obtenerValor())
            self.inorder(nodoActual.obtenerHijoDerecho())
    def postorder(self,nodoActual):
        """Descripción de la función
        Parameters
        ----------
        parametro_1 : tipo
            Descripción del parametro
        parametro_2 : tipo
            Descripción del parametro
        Returns
        -------
        tipo
            Descripción de los valores que devuelve
        """
        if nodoActual is not None:
            self.postorder(nodoActual.obtenerHijoIzquierdo())
            self.postorder(nodoActual.obtenerHijoDerecho())
            print("Llave:",nodoActual.obtenerLlave()," | Valor:",nodoActual.obtenerValor())
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
arbol.inorder(arbol.obtenerRaiz())
arbol.insertar(17)#2
arbol.insertar(17)#3
arbol.insertar(17)#4
arbol.inorder(arbol.obtenerRaiz())


