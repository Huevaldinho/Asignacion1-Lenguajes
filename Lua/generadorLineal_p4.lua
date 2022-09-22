
-- Generador de números pseudoaleatorios
-- Fuente: Dromey, 'How to solve it by computer'
-- Algorithm 3.6, 'Generation of pseudo-random numbers'
-- Adaptado para Python por Ignacio Trejos Zelaya
-- Modificado por Alonso Garita Granados
-- Implementado en Lua por Raquel Arguedas
-- Fecha de inicio 15/09/2022
-- Fecha de finalización 20/09/2022

co = coroutine.create(
	function (semilla, n)
		-- si la semilla es menor a 11 la convierte en 11
		if(semilla < 11)then 
        	semilla = 11
		end

		-- La literatura  explica la importancia de elegir bien los valores m, a y b
		m = 4096 -- período
    	a = 109  -- multiplicador
    	b = 853  -- incremento
		
		-- busca el próximo primo
		x = semilla
		flag = 1
		while (flag == 1) do
			flag = 0
			for var=2,9 do
   				if x%var == 0 then
					flag = 1
					x = x + 1
				end
				if flag == 1 then break end
			end
		end 

		for i=0,n-1 do
			-- devolver el siguiente número aleatorio
			coroutine.yield(x)

        	-- calcular el siguiente número aleatorio
        	x = (a * x + b) % m
		end
	end
)

-- para realizar pruebas
n=5
semillaX=555

for i=0,n-1 do
	isAlive, value = coroutine.resume(co, semillaX, n)
	print(value)
end

