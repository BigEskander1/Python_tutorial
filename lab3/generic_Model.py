import numpy as np

M = np.array([[X,Y,Z,A] for X in range(2) for Y in range(2) for Z in range(2) for A in range(2)])
print(M)


def step(x):
    return 1 if x >= 0 else 0

# generic Neuron
def neuron(x , w , b):
    return step ( x @ w + b )   # =  step(np.dot(x , w ) + b) 

def and_P(x): # x is vector
    n = neuron(x , np.array([1,1]) , -2 )
    return n
 
def GM_P(x):
    n1 = neuron(x[[0,2,3]] , np.array([-1,1,1]) , -2)
    n2 = neuron(x[[1,3]] , np.array([-1,1]) , -1)
    m1 = neuron(np.array([n1,n2]) , np.array([1,1]) , -1)
    n3 = neuron(x[[0,1]] , np.array([1,1]) , -2)
    n4 = neuron(x[[0,2]] , np.array([1,1]) , -2)
    m2 = neuron(np.array([n3,n4]) , np.array([1,-1]) , 0)
    return neuron(np.array([m1,m2]) , np.array([1,1]) , -2)

def test_GM_P(m):
    return int( ((m[3] and not(m[0]) and m[2] ) or ( m[3] and not(m[1])) )and ((m[0] and m[1]) or not(m[0] and m[2]) ))
for m in M:
    print(f"GM_P {GM_P(m)} and test {test_GM_P(m)}")