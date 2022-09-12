
#Fecha Creación 11/09/2022


class Node:
    ###Nodo de un arbol.

    

    def __init__(self, data):
        ##Los hijos se crean nulos.
        self.left = None##hijo izquierdo
        self.right = None##hijo derecho
        self.data = data##datos del nodo


    ##Recorridos del arbol
    ##-------------------------------------------------#
    def preorder(self,node):
        ##Recorre el arbol node en sentido raiz - hijo izquierdo - hijo derecho.
        ## node Node: Recibe un objeto de tipo Node.
        ##Cuando la recursion llega a una hoja no entra en el if node
        ##entonces la recursion se regresa para continuar con el recorrido.
        
        if node:
            print(node.data)
            node.preorder(node.left)
            node.preorder(node.right)

    def inorder(self,node):
        if node:
            node.inorder(node.left)
            print(node.data)
            node.inorder(node.right)
    def postorder(self,node):
        if node:
            node.postorder(node.left)
            node.postorder(node.right)
            print(node.data)
    ##-------------------------------------------------#
##Crea la raiz del arbol con dato = 10
root = Node(10)
##Inserta 34 en el hijo izquierdo
root.left = Node(34)
##Inserta 89 en el hijo derecho
root.right = Node(89)
##Al hijo izquierdo inserta 45 en el nodo izquierdo.
root.left.left = Node(45)
##Al hijo derecho inserta 50 en el nodo derecho.
root.left.right = Node(50)

root.inorder(root)##Llama el metodo in order para imprimir el arbol

x = None##Declara una variable de tipo NoneType
if x:##Cuando el arbol tiene un objeto como hijo entonces hace el orden
    print("x es NoneType")
else:##Si el nodo que entra es None entonces la recursion se regresa.
    print("x es otro tipo de dato")
    ##Si el nodo es una hora no la recursion se empieza a devolver 
    