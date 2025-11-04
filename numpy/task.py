import numpy as np 
array = np.arange(1 , 31)
# print(array)
reshaped = array.reshape((6,5))
print(reshaped)
print('-------------------------------------------------dd')

print(reshaped.diagonal(offset=1))
print('-------------------------------------------------')
print(reshaped[2:4 , 0:2])
print('-------------------------------------------------')

print(reshaped[0::5,1::5])

print('-------------------------------------------------')

print(reshaped[-2:0,3:5])
print('-------------------------------------------------')


def is_prime(n):
    if n <=1:
        return False
    for i in range(2 ,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

print('-------------------------------------------------')
primes = [x for x in range(1100) if is_prime(x) ]
# print(primes[0:50])
