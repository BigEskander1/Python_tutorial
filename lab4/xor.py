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



def XOR_4(x):  # x = [A, B, C, D]
    a, b, c, d = x
    xor1 = XOR_MLP(np.array([a, b]))
    xor2 = XOR_MLP(np.array([xor1, c]))
    return XOR_MLP(np.array([xor2, d]))


X = [[a, b, c, d] for a in range(2)
                  for b in range(2)
                  for c in range(2)
                  for d in range(2)]
    
for x in X:
        print(f"{x} -> XOR_4 = {XOR_4(np.array(x))}, expected = {x[0]^x[1]^x[2]^x[3]}")


def XOR_lin(x):
     n = XOR_MLP(x[[0,1]])
     for i in range(2,len(x)):
          n = XOR_MLP(np.array([n,x[i]]))
     return n
def Real_xor_lin(x):
     n = x[0] ^ x[1]
     for i in range(2,len(x)):
          n = n ^ x[i]
     return n


X = np.array([[a,b,c,d] for a in range(2) for b in range(2) for c in range(2) for d in range(2)])

print('----------------------------------------------')

for x in X :
    print(f"Bool fun of {x} = {XOR_lin(x)} , expected({Real_xor_lin(x)})")