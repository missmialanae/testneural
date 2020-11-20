#all numbers are random
import numpy as np
#input connections for the neuron; other neurons are feeding into it
input = [1.2, 5.1,2.1]

#each input has a weight
weights = [ [0.4, 0.5, 0.6],
			[-0.4, -0.5, -0.6],
			[-0.34, 0.99, 0.17]
			]

#every unqiue neuron has a bias; 
bias = [3,2,0.5]

#adding more neurons 

#the output for this would be the weights * input + bias; 
output = np.dot(weights, inputs)+biases

print(output)