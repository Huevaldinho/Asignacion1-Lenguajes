--[[
Ejemplos de Corrutinas en Lua
Creadores
    Garita Granados Alonso - 2021030220
    Sanabria Solano María Fernanda - 2021005572 
    Arguedas Sánchez Raquel Marcela - 2021032567
    Obando Arrieta Felipe de Jesús - 2021035489
Fecha Creación: 20/09/2022
Ultima Modificacion: 21/09/2022
]]


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
  
--   print("main", coroutine.resume(co, 3, 2))
--   print("main", coroutine.resume(co, 12,14))
--   print("main", coroutine.resume(co, 5, 6))
--   print("main", coroutine.resume(co, 10, 20))
 
 
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
 
--  for index = 1, 10 do
--     print(index, getNumber())
--  end