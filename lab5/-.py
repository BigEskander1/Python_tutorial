import numpy as np 


class Perceptron:
    def __init__(self,input_size):
        self.weights = np.zeros(input_size)
        self.bias = 0
        
    @staticmethod
    def step(x):
        return 1 if x >= 0 else 0 
    
    def predict(self,x):
        return Perceptron.step(x @ self.weights + self.bias)
    
    def train(self,X,y):
        for _ in range(10):
            for i,x in enumerate(X):
                y_hat = self.predict(x)
                self.weights = self.weights + (y[i] - y_hat) * X
                self.bias = self.bias + (y[i] - y_hat) 

X = [[a,b] for a in range(2) for b in range(2)]
X = np.array(X)

y_and = [0,0,0,1]
y_and = np.array(y_and)

