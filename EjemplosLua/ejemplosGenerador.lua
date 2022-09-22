--[[
Ejemplos de Generadores en Lua
Creadores
    Garita Granados Alonso - 2021030220
    Sanabria Solano María Fernanda - 2021005572 
    Arguedas Sánchez Raquel Marcela - 2021032567
    Obando Arrieta Felipe de Jesús - 2021035489
Fecha Creación: 20/09/2022
Ultima Modificacion: 21/09/2022
]]

--[[
Ejemplo 1 generadores
Fuente: tutorialspoint. (s. f.). Example Coroutine [Software]. https://www.tutorialspoint.com/lua/lua_iterators.htm
]]
function square(iteratorMaxCount,currentNumber)

    if currentNumber<iteratorMaxCount 
    --Si el contador aun no llega al maximo, sigue con el proceso
    then
       -- Se aumenta el contador y se devuelve este al cuadrado
       currentNumber = currentNumber+1
       return currentNumber, currentNumber*currentNumber
    end
      
end
  
-- for i,n in square,3,0 do
--     print(i,n)
-- end
 
 
 
--[[
Ejemplo 2 generadores
Fuente: tutorialspoint. (s. f.). Example Stateful Iterators [Software]. https://www.tutorialspoint.com/lua/lua_iterators.htm
]]
 
array = {"Lua", "Tutorial"}
 
function elementIterator (collection)
    -- Clausura para guardar los valores para la siguiente llamada
    local index = 0
    local count = #collection
     
    -- The closure function is returned
     
    return function ()
       index = index + 1
         
       if index <= count
       then
          -- return the current element of the iterator
          return collection[index]
       end
         
    end
     
end
 
-- for element in elementIterator(array)
-- do
-- print(element)
-- end