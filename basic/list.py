things = [ 1 , (1,2) , 'Ahmed' , [2,3] ]
print('first index has ' , things[0]);
print('last index has ' , things[-1]);

things.append('a');
print(things);

things.insert(2 , 'fady');
print(things);


del(things[3]);
print(things);

print(things.pop())
print(things);

print(things.pop(0))  #first element
print(things);

things.remove((1,2));
print(things)

things = [ 'aa' , 'b' , 'c' , 'a' , 'd' , 'zzzz' ];
things.sort()
print(things)

things = [ 'aa' , 'b' , 'c' , 'a' , 'd' , 'zzzz' ];
things.sort(reverse=True)
print(things)

things.reverse()
print('after reverse' , things)

print(len(things))

print(list('python')) # constructor to do list

print(list(enumerate(things))) # unpacking seq (index , value)

for index , thing in enumerate(things):
    print('in index' , index , 'thing is ' , thing)


print(list(range(5)))
print(list(range(1,5)))
print(list(range(1,6)))
print(list(range(1, 15, 2))) # (start , stop i never be it , step skip 2 element every time)


even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    squares.append( value ** 2)

print(squares)

# list comprehensions is create list in one line
squares = [sq**2 for sq in range(1,11)]
print(squares)

# slicing
print('slice squares[0:3]    :    ',  squares[0:3])
print('slice squares[:3]     :    ',squares[:3])
print('slice squares[3:10]   :    ' ,squares[3:10])
print('slice squares[3:]     :    ', squares[3:])

print('slice squares[0:10:2] :    ' , squares[0:10:2])



# copy


# 1- copy without copy method has a problem if you add or delete because in the same memory
my_char = ['F' , 'A' , 'D' , 'Y' , 'M' , 'O' , 'U' , 'N' , 'E' , 'R']
your_char = my_char 
your_char.append('C')
print(my_char)
print(your_char)

# 2- copy with copy method
my_char = ['F' , 'A' , 'D' , 'Y' , 'M' , 'O' , 'U' , 'N' , 'E' , 'R']
your_char = my_char[:]
your_char.append('C')
print(my_char)
print(your_char)