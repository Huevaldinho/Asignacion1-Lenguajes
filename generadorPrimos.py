#Proyecto Lenguajes
#Punto 5.

def generarPrimos(n):
    isPrimo = True
    primos = []
    i = 0 #Contador para generar n primos
    m = 2 #Candidatos a primos

    while (i < n): #Range(n-1) hace que i esté en el rango [2, n], de lo contrario estaría en [2, n+1]
        for p in primos:
            if(m % p == 0): #Chequea si es divisible entre otro primo averiguado
                isPrimo = False
                break

        if(isPrimo): #Si es primo:
            primos.append(m) #Lo agrega
            yield m #Lo libera
            i+=1 #Incrementa el contador
        else:
            isPrimo = True
        m+=1 #Siguiente candidato

    return None

def main():
    for p in generarPrimos(50):
        print(p)
    return None

main()