# f = y'z' + w'xy' + x'yz'
import numpy as np

def step(x):
    return 1 if x >= 0 else 0

# generic Neuron
def neuron(x , w , b):
    return step ( x @ w + b )   # =  step(np.dot(x , w ) + b) 

def and_P(x): # x is vector
    n = neuron(x , np.array([1,1]) , -2 )
    return n


X = [[0,0],[0,1] , [1,0] , [1,1]] 
X = [[a,b,c,d] for a in range(2) for b in range(2) for c in range(2) for d in range(2)]
print(X)

X = np.array(X)


def And(x,w):
    l = sum(a for a in w if a > 0)
    n = neuron(x,w,-l)
    return n
def OR(x,w):
    l = sum(a for a in w if a > 0)
    n = sum(abs(a) for a in w )
    b = - (l-n+1)
    return neuron(x,w,b)


def BoolFun(x):
    n1 = And(x[[1,2]] , np.array([-1,-1]))
    n2 = And(x[[0,1,3]] , np.array([1,-1,-1]))
    n3 = And(x[[0,2]] , np.array([-1,-1]))
    return OR(np.array([n1,n2,n3]) , np.array([1,1,1]))

def RealBoolFun(x):
    return((not x[1] and not x[2] ) or (x[0] and not x[1] and not x[3]) or (not x[0] and not x[2]) )


X = np.array([[a,b,c,d] for a in range(2) for b in range(2) for c in range(2) for d in range(2)])

for x in X :
    print(f"Bool fun of {x} = {BoolFun(x)} , expected({RealBoolFun(x)})")