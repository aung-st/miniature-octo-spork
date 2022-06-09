import numpy as np 
from sklearn.datasets import make_regression
#4 feature input into 2 hidden layers of 3 neurons each
inputs = [[2,2,4,6],
          [1,4,-2,3],
          [1,5,7,3]]
weights = [[0.1,0.1,0.1,0.1],[0.5,0.5,0.5,0.5],[0.3,0.2,0.4,0.6]]
biases = [2,3,0.2]
weights2 = [[0.3,0.5,-2],[-2,5,-1],[2,0.4,0.6]]
biases2 = [-1,2,-3]

layer1_outputs = np.dot(inputs,np.array(weights).T ) + biases
print(layer1_outputs)

layer2_outputs = np. dot (layer1_outputs, np. array(weights2).T) + biases2
print(layer2_outputs)

# Fully connected layer
class FC:
    # Layer initialization
    def __init__ (self,n_inputs,n_neurons ):
        self.weights = 0.01 * np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros((1,n_neurons))
    #Foward pass
    def forward (self,inputs):
        self.output = np.dot(inputs, self .weights) + self.biases

n_inputs = 3
n_neurons = 5

print(weights)
print(biases)

# Create Dense layer with 2 input features and 3 output values
fc1 = FC(2,3)

# Create dataset
# Sample size
M = 3
# No. of input features
n = 2
X, y = make_regression(n_samples=M, n_features=n, n_informative=n,n_targets=1, random_state=42)

# Perform a forward pass of our training data through this
fc1.forward (X)
# Let's see output of the first few samples:
print (fc1.output[: 5 ])