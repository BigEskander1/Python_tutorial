# sets is unordered seq and mutable (can change and add)

set1 = {1,2,3,4,5,6,5,6,6,7,7,7,7,7}
print(set1) 


# check duplicate
list = [1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,4,4,4,5,5,6,]
my_set = set(list)
print('list has : ' , list.__len__() , 'item')
print('set has : ' , my_set.__len__() , 'item')


# mutable can add and change
set1.add(8)
print(set1)

# union , insertion  , difference and symmetric diff
A = {1,2,4,7}
B = {4,7,8,9}

print('A = ' ,A)
print('B = ' ,B)

print('A union B =  ' ,A | B)
print('A union B =  ' ,A.union(B))
print('B union A =  ' ,B.union(A))

print('A intersection B =  ' ,(A & B))
print('A intersection B =  ' , A.intersection(B))
print('A intersection B =  ' ,B.intersection(A))

print('A difference B =  ' ,A - B)
print('B difference A =  ' ,B - A)
print('A difference B =  ' ,A.difference(B))
print('B difference A =  ' ,B.difference(A))

print('A symmetric difference B =  ' ,A ^ B)
print('A symmetric difference B =  ' ,A.symmetric_difference(B))

for num in A: 
    print(num)

print(2 in A)
print(2 in B)