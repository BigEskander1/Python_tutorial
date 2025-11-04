# xy' + x'y
# (x+y)(x'+y')

import numpy as np
def step(x):
    return 1 if x >= 0 else 0

# generic Neuron
def neuron(x , w , b):
    return step ( x @ w + b )   # =  step(np.dot(x , w ) + b) 

def XOR_MLP(x): # x is vector
    n1 = neuron(x ,np.array([1,-1]) , -1 )
    n2 = neuron(x ,np.array([-1,1] ), -1 )
    n3 = neuron(np.array([n1,n2]) , np.array([1,1]) , -1)
    return n3



def XOR(x):
    return {x[0] ^ x[1]}


X = [[a,b] for a in range(2) for b in range(2)]
# print(X)
X = np.array(X)

for x in X: 
    print(f"XOR_MLP(X)  = {XOR_MLP(x)}  , XOR {x[0] ^ x[1]}" )



def XOR_MLP2(x): # x is vector
    n1 = neuron(x ,np.array([1,1]) , -1 )
    n2 = neuron(x ,np.array([-1,-1] ), 1 )
    n3 = neuron(np.array([n1,n2]) , np.array([1,1]) , -2)
    return n3


print("----------------------------------")
for x in X: 
    print(f"XOR_MLP2(X)  = {XOR_MLP2(x)}  , XOR {x[0] ^ x[1]}" )



def OR_P():
    n1 = neuron(x ,np.array([1,1]) , 1 )
    return n1


    