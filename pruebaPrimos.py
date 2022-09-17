
# Python program to print all
# prime number in an interval
 
def prime(x):
    prime_list = []
    i = 2
    while len(prime_list) <= x:
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
        i+=1
    return prime_list
 
# Driver program
size = 1199
lst = prime(size)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)
    