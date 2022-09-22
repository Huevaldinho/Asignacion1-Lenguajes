--[[
Ejemplos de Iteradores en Lua
Creadores
    Garita Granados Alonso - 2021030220
    Sanabria Solano María Fernanda - 2021005572 
    Arguedas Sánchez Raquel Marcela - 2021032567
    Obando Arrieta Felipe de Jesús - 2021035489
Fecha Creación: 20/09/2022
Ultima Modificacion: 21/09/2022
]]

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