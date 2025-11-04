# numpy (numerical python)
# soo fast (in memory)
import numpy as np 
import sys 
# print(np.__version__)

my_list = [1,2,3,4]
my_list = my_list*2
print(my_list)

print('-----------------------------------------')

array = np.array([1,2,3,4])
print(array)
print(np.append(array , np.array([9])))


print(type(array))

print('-----------------------------------------')

array = array*2
print(array)

print('-----------------------------------------')


array = np.array('A')
print(array.ndim) # num of dimension
array = np.array(['A' , 'B' , 'C'])
print(array.ndim) # num of dimension
array = np.array([['A' , 'B' , 'C'],
                 ['D' , 'E' , 'F'],
                 ['G' , 'H' , 'I']])
print(array.ndim) # num of dimension

array = np.array([[['A' , 'B' , 'C'],['D' , 'E' , 'F'],['G' , 'H' , 'I']] ,
                 [['J' , 'K' , 'L'],['M' , 'N' , 'O'],['P' , 'Q' , 'R']],
                 [['S' , 'T' , 'U'],['V' , 'W' , 'X'],['Y' , 'Z' , ' ']]])
print(array.ndim) # num of dimension

print(array[0,1,1])


# scaler arithmetic
array = np.array([1,2,3,4])
print(array + 1 )
print(array - 3 ) # for each element

# vectorized math func
print(np.sqrt(array))
print(np.round(np.sqrt(array))) 
print(np.pi)


print('-----------------------------------------------------')
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
print(array.shape)
print(array.ndim)
print(array.size)
print(array[1,1])
print(array[:,0])

print('-----------------------------------------------------')
array = np.array((1,2,3,4))
print(array)




print('-----------------------------------------------------')
np.zeros((2,3))
np.ones((4,2))



np.full((2,2) , 42)

np.full_like(array,23)

print('-----------------------------------------------------')

print(np.random.rand(2,2))
print('-----------------------------------------------------')
print(np.random.randint(-8,9 ,size=(3,4)) )

print('-----------------------------------------------------')
print(np.identity(4))


print('-----------------------------------------------------')
array = np.array([[1,2,3,4],[5,6,7,8]])
array2 = np.repeat(array , 3 , axis=0) # every row repeat
print(array2)

print('-----------------------------------------------------')

array = np.array([[1,2,3,4],[5,6,7,8]])
array2 = np.repeat(array , 3 , axis=1) # every row repeat , axis 0 rows , axis 1 col(default)
print(array2)

print('-----------------------------------------------------')
array = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],
                  [[13,14,15,16],[17,18,19,20],[21,22,23,24]]
                  ,[[25,26,27,28],[29,30,31,32],[33,34,35,36]]])
print(np.max(array,axis=1))

print('-----------------------------------------------------')
array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(np.max(array,axis=1)) # max num in each row



