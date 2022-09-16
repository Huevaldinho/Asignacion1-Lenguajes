
--Fecha Creacion: 13/09/2022
--Ultima Modificacion: 13/09/2022



function isPrime(x)
 
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

co = coroutine.create(function (num)
   
    list = {}
    size = 1  
    i = 2
    while true do --Sale cuando list tenga tamanno num
        if isPrime(i) then --Si i es primo se agregaa a list
            print(coroutine.status(co))
            coroutine.yield(i)
            size = size+1
        end
        if size>num then
            print("Sali mal lol")
            return
        end
        
        i = i + 1 --Se aumenta i
    end
    print("Sali mal lol")
    return  --Retornamos
end)

function main(num)
    for i=1,num do
        -- print("Numero " , i, ": ",coroutine.resume(co, num))
        print(coroutine.resume(co, num))
        print(coroutine.status(co))
    end
    print(coroutine.status(co))
    print("Terminamos en el main")
    return 
end

main(5)

-- n = 1200 --Tamanno de la lista
-- lst = generator(n) --lista con primos retornada dela funcion
-- print("The prime numbers in this range are: ", table.concat(lst, ","))

