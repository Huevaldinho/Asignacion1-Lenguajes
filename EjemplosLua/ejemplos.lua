--[[
Creadores
    Garita Granados Alonso - 2021030220
    Sanabria Solano María Fernanda - 2021005572 
    Arguedas Sánchez Raquel Marcela - 2021032567
    Obando Arrieta Felipe de Jesús - 2021035489
Fecha Creación: 20/09/2022
Ultima Modificacion: 21/09/2022
]]


-- Corrutinas!
--[[
Ejemplo 1 Corrutina
Fuente: tutorialspoint. (s. f.). Example Coroutine [Software]. https://www.tutorialspoint.com/lua/lua_coroutines.htm
]]

co = coroutine.create(function (value1,value2)
   --Primer parte de la corrutina
    local tempvar3 = 10
    print("coroutine section 1", value1, value2, tempvar3)
   
   --Segunda parte de la corrutina
    local tempvar1 = coroutine.yield(value1+1,value2+1)
    tempvar3 = tempvar3 + value1
    print("coroutine section 2",tempvar1 ,tempvar2, tempvar3)
     
   --Tercera parte de la corrutina
    local tempvar1, tempvar2= coroutine.yield(value1+value2, value1-value2)
    tempvar3 = tempvar3 + value1
    print("coroutine section 3",tempvar1,tempvar2, tempvar3)

   --Ultima parte de la corrutina
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
      -- Devuelve los valores
      coroutine.yield(1)
      coroutine.yield(2)
      coroutine.yield(3)
      coroutine.yield(4)
      coroutine.yield(5)
      end)
      return co
   end
	
   if(numberHelper) then
      -- Si la corrutina existe, al continua
      status, number = coroutine.resume(numberHelper);
		
      if coroutine.status(numberHelper) == "dead" then
         -- Si la corrutina termino, llama a crearla
         numberHelper = getNumberHelper()
         status, number = coroutine.resume(numberHelper);
      end
      return number
   else
      -- Si la corrutina no existe, llama a crearla
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
-- Key corresponde al contador y value al valor en esa posicion
for key,value in ipairs(array) 
do
   print(key, value)
end

 --[[
Ejemplo 2 iteradores
Fuente:  Ierusalimschy R., (s. f.). Stateless Iterators [Software]. http://www.lua.org/pil/7.3.html#:~:text=When%20Lua%20calls%20ipairs%20%28a%29%20in%20a%20for,in%201%2C%20a%20%28unless%20a%20is%20already%20nil%29.
]]
array = {"Lua", "Tutorial"}
-- Key corresponde al contador y value al valor en esa posicion
for key,value in next, array
do
   print(key, value)
end

-- Generadores!
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
 
for i,n in square,3,0
do
   print(i,n)
end



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

for element in elementIterator(array)
do
   print(element)
end