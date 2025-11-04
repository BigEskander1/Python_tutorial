print("Welcome to CS417") # println
print("Welcome to CS417" , "welcome to CS417") # in the same line
x = 4
print("x is", x)
print(type(x)) # every thing is object in python
z = 'c'
print(type(z)) # there is no char here
z = 1.5 # we can change the type
print(type(z))

print(f"x = {x} , y = {z}")



a = "abc"
print(f" length of a is {len(a)}")



# # input
# a = input("Enter a number: ")
# b = input("Enter another number: ")
# # you must casting because is string
# # print(f"x = {x} , y = {y}")
#
#
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# print(f"a = {a} , b = {b}")
#

x = 3 > 7
print(type(x))

# x = int(input("Enter a number: "))
#
# # tap is important here
# if x > 7:
#     print("x is greater than 7")
# elif x < 7:
#     print("x is less than 7")
# else:
#     print("x is equal to 7")
#
# print("end")

print("--------------------------------------------------------------------------")

for i in range(10):
    print( f"i is {i}" )
print("end")

print("--------------------------------------------------------------------------")

for i in range(5 , 10  , 2 ): # start(default  0) end step(default  1)
    print( f"i is {i}" )

print("--------------------------------------------------------------------------")
for i in range(5 , -10  , -2 ):
    print( f"i is {i}" )

print("--------------------------------------------------------------------------")


s = "Bigeskander"
for c in s:
    print(c)

print("--------------------------------------------------------------------------")


x = 10
y = 5
while x > 1 and y > 1: # and , or
    print( f"x is {x} and y is {y}")
    x -= 1
    y -= 1

print("--------------------------------------------------------------------------")

x = 10
y = 5
while x > 1 or y > 1: # and , or
    print( f"x is {x} and y is {y}")
    x -= 1
    y -= 1

print("--------------------------------------------------------------------------")

for _ in range(10): # i don't care about i
    print( "hello " , end='\t' ) # make it print not println
print()

print("--------------------------------------------------------------------------")


def func1():
    print("func1")

func1()
func1()

def fun2(x , y , z = 5):
    print(f"x is {x}, y is {y}, z is {z}")
    return x + y + z

a = fun2(y =1 , x = 3 , z = 4)
print(a)

print("--------------------------------------------------------------------------")

def fun2(x , y , z = 5):
    print(f"x is {x}, y is {y}, z is {z}")
    return (x + y ) , (y + z ) , (x + z )

a , b , c = fun2(x = 2 , y = 3 , z = 5)
print(a)
print(b)
print(c)

a = fun2(x = 2 , y = 3 , z = 4)
print(a)

# swap
a = 3
b = 4
a , b = b ,a
print(f" a is {a} and b is {b}")


print("--------------------------------------------------------------------------")
# list ( mutable can change , order keep what you insert by order  )
a = [1 , 2 , "Eskander" , True ,1 , 2 , "Eskander" , True]
for x in a:
    print(x)

print(a[2:4])
print(a[2:7:2])
print(a[2:])
print(a[:3])
print(a[-1::-1])
print("--------------------------------------------------------------------------")

# tuple ( order , immutable we can't change)
a = (1,3,4,5,12)

print("--------------------------------------------------------------------------")


# dictionary  { key  (unique , immutable) : value (anything) } ( order , immutable we can't change)
d = { 1 : "one" , 2 : "two" , 3 : "three" }
print( d[2])

print("--------------------------------------------------------------------------")



