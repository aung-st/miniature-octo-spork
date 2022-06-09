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

class ReLU:
    # Forward pass
    def forward (self,inputs):
    # Calculate output values from input
        self.output= np.maximum( 0 , inputs)

# Create ReLU activation (to be used with fc layer):
activation1 = ReLU()

# Perform a forward pass of our training data through this
fc1.forward(X)
activation1.forward(fc1.output)




# Let's see output of the first few samples:
print (fc1.output[: 5 ])


layer_outputs = [ 4.4 , 2.21 , 2.585 ]
# For each value in a vector, calculate the exponential value


class Activation_Softmax :
    # Forward pass
    def forward ( self , inputs ):
        # Get unnormalized probabilities
        exp_values = np. exp (inputs - np. max (inputs, axis =1 ,keepdims = True ))
        # Normalize them for each sample
        probabilities = exp_values / np. sum (exp_values, axis= 1 ,keepdims = True )
        self .output = probabilities

softmax = Activation_Softmax ()
softmax.forward ([[ 1 , 2 , 3 ]])
print (softmax.output)

softmax.forward ([[ - 2 , - 1 , 0 ]]) # subtracted 3 - max from the list
print (softmax.output)

softmax.forward ([[ 0.5 , 1 , 1.5 ]]) #changes confidence 
print(softmax.output)

# Create second Dense layer with 3 input features (as we take output
# of previous layer here) and 3 output values
fc2 = FC(3,4)
# Create Softmax activation (to be used with Dense layer):
activation2 = Activation_Softmax ()

# Make a forward pass through second Dense layer
# it takes outputs of activation function of first layer as inputs
fc2.forward(activation1.output)
# Make a forward pass through activation function
# it takes the output of second dense layer here
activation2.forward(fc2.output)
# Let's see output of the first few samples:
print (activation2.output[: 5 ])
