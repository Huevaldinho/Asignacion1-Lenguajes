
-- Fecha Creacion: 13/09/2022
-- Ultima Modificacion: 19/09/2022



function isPrime(x)
    --[[
    Determina si x es o no primo

    Parametros:
        -x (int): Numero a determinar.

    Retorna:
        boolean: True si es primo, False si no.
    ]]
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
   --[[
    Genera numeros primos

    Parametros:
        -Ninguno.

    Libera:
        Tuple: Tuple con True y el número si pudó liberar el número.
    ]]
    i = 2
    while true do --Ciclo para generar los números
        if isPrime(i) then --Si i es primo se libera el número
            coroutine.yield(i)--Se libera el número
        end
        
        i = i + 1 --Se aumenta i
    end
    return  --Retornamos
end)

function main(num)
    for i=1,num do
        print("Numero " , i, ": ",coroutine.resume(co, num))
    end
    print("Terminamos en el main")
    return 
end

main(5)



