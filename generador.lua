function isPrime(x)
    if x == 0 or x == 1 then
        return false
    elseif x == 2 then
        return true
    end
    for j = 2, math.floor(x/2)+1 do
        if x % j == 0 then
            return false
        end
    end
    return true
end

function generator(num)
    prime_list = {}
    size = 1
    i = 2
    while (size <= num) do
        if isPrime(i) then
            prime_list[size] = i
            size = size + 1
        end
        i = i + 1
    end
    return prime_list
end

n = 1200
lst = generator(n)
print("The prime numbers in this range are: ", table.concat(lst, ","))

