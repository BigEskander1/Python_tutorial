# x and y as a P
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
X = [[a,b] for a in range(2) for b in range(2)]
print(X)
X = np.array(X)

for x in X: 
    print(f"And P(X)  = {and_P(x)} , AND{x} = {x[0] and x[1]} ")