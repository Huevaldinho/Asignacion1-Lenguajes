/*
Fecha Creacion: 13/09/2022
Ultima Modificacion: 13/09/2022
*/


function isPrime(x)
    /*
    Funcion:
        Define si x es primo o no
    Parametros:
        int x:
            Numero que se evaluo si es o no primo
    Retorna:
        boolean:
            True si x es primo, false si no
    */
    if x == 0 or x == 1 then --0 y 1 no son numeros primos
        return false
    elseif x == 2 then --Primer numero primo
        return true
    end
    for j = 2, math.floor(x/2)+1 do --Se recorren posibles divisores de x
        if x % j == 0 then
            return false -- Se encuentra un divisores
        end
    end
    return true -- No se encontraron divisores
end

function generator(num)
    /*
    Funcion:
        Devuelve una lista de tamanno num con numeros primos consecutivos
    Parametros:
        int num:
            Tamanno de la lista a devolver
    Retorna:
        lista:
            Lista con numeros primos de tamanno num
    */
    list = {}
    size = 1  
    i = 2
    while (size <= num) do --Sale cuando list tenga tamanno num
        if isPrime(i) then --Si i es primo se agregaa a list
            prime_list[size] = i --Se agrega i a list
            size = size + 1 -- Se aumenta el contador de size de la lista
        end
        i = i + 1 --Se aumenta i
    end
    return prime_list --Retorna la lista
end

n = 1200 --Tamanno de la lista
lst = generator(n) --lista con primos retornada dela funcion
print("The prime numbers in this range are: ", table.concat(lst, ","))

