-- Corrutinas!
--[[
Ejemplo 1 Corrutina
Fuente: tutorialspoint. (s. f.). Example Coroutine [Software]. https://www.tutorialspoint.com/lua/lua_coroutines.htm
]]

co = coroutine.create(function (value1,value2)
    local tempvar3 = 10
    print("coroutine section 1", value1, value2, tempvar3)
     
    local tempvar1 = coroutine.yield(value1+1,value2+1)
    tempvar3 = tempvar3 + value1
    print("coroutine section 2",tempvar1 ,tempvar2, tempvar3)
     
    local tempvar1, tempvar2= coroutine.yield(value1+value2, value1-value2)
    tempvar3 = tempvar3 + value1
    print("coroutine section 3",tempvar1,tempvar2, tempvar3)
    return value2, "end"
     
 end)
 
 print("main", coroutine.resume(co, 3, 2))
 print("main", coroutine.resume(co, 12,14))
 print("main", coroutine.resume(co, 5, 6))
 print("main", coroutine.resume(co, 10, 20))


--[[
Ejemplo 2 Corrutina
Fuente: tutorialspoint. (s. f.). Example Coroutine [Software]. https://www.tutorialspoint.com/lua/lua_coroutines.htm
]]

function getNumber()
    local function getNumberHelper()
       co = coroutine.create(function ()
       coroutine.yield(1)
       coroutine.yield(2)
       coroutine.yield(3)
       coroutine.yield(4)
       coroutine.yield(5)
       end)
       return co
    end
     
    if(numberHelper) then
       status, number = coroutine.resume(numberHelper);
         
       if coroutine.status(numberHelper) == "dead" then
          numberHelper = getNumberHelper()
          status, number = coroutine.resume(numberHelper);
       end
         
       return number
    else
       numberHelper = getNumberHelper()
       status, number = coroutine.resume(numberHelper);
       return number
    end
     
 end
 
 for index = 1, 10 do
    print(index, getNumber())
 end

 -- Iteradores!
 --[[
Ejemplo 1 iteradpores
Fuente: tutorialspoint. (s. f.). Example Coroutine [Software]. https://www.tutorialspoint.com/lua/lua_iterators.htm
]]
array = {"Lua", "Tutorial"}

for key,value in ipairs(array) 
do
   print(key, value)
end

 -- Iteradores!
 --[[
Ejemplo 2 iteradpores
Fuente: tutorialspoint. (s. f.). Example Coroutine [Software]. https://www.tutorialspoint.com/lua/lua_iterators.htm
]]
function square(iteratorMaxCount,currentNumber)

    if currentNumber<iteratorMaxCount
    then
       currentNumber = currentNumber+1
       return currentNumber, currentNumber*currentNumber
    end
     
 end
 
 for i,n in square,3,0
 do
    print(i,n)
 end

-- Generadores!
-- Ejemplo 1 generadores

co = coroutine.create(function ()
    
     i = 0
     while true do --Ciclo para generar los números
         coroutine.yield(i)--Se libera el número
         i = i + 1 --Se aumenta i
     end
     return  --Retornamos
 end)
 
 num = 5
 for i=1,num do --For para imprimir num cantidad de números
    estatusLocal, valor = coroutine.resume(co) --Consumidor del generador de números
    print("Numero " , i, ": ",valor)--Impresion de número
end

--[[
Ejemplo 2 generadores
Fuente: tutorialspoint. (s. f.). Example Coroutine [Software]. https://www.tutorialspoint.com/lua/lua_coroutines.htm
Modificado por Maria Fernanda Sanabria para simplificar su proceso.
]]

function getNumber()
    local function getNumberHelper()
       co = coroutine.create(function ()
       coroutine.yield(1)
       coroutine.yield(2)
       coroutine.yield(3)
       coroutine.yield(4)
       coroutine.yield(5)
       end)
       return co
    end

     
 end
 
 for index = 1, 5 do
    print(index, getNumber())
 end