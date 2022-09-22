-- Fecha Creacion: 13/09/2022
-- Ultima Modificacion: 19/09/2022
--[[
Creadores
    Garita Granados Alonso - 2021030220
    Sanabria Solano María Fernanda - 2021005572 
    Arguedas Sánchez Raquel Marcela - 2021032567
    Obando Arrieta Felipe de Jesús - 2021035489
Fecha Creación: 20/09/2022
Ultima Modificacion: 21/09/2022
]]


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

co = coroutine.create(function ()
   --[[
    Genera numeros primos

    Parametros:
        -Ninguno.

    Libera:
        Tuple: Estado de la corrutina y el número primo.
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
    --[[
    Imprime num cantidad de números primos del generador

    Parametros:
        -num(int): Cantidad de números primos a imprimir.

    Retorna:
        
    ]]
    for i=1,num do --For para imprimir num cantidad de números primos
        estatusLocal, valor = coroutine.resume(co) --Consumidor del generador de números primos
        print("Numero " , i, ": ",valor)--Impresion de número primo
    end
    print("FIN")
    return 
end

main(5)



