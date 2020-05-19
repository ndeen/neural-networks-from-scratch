# our first neuron

# these inputs represent outputs from the previous layer
inputs = [1.2, 5.1, 2.1]

# each unique input has a unique weight associated with it
weights = [3.1, 2.1, 8.7]

# each neuron has its own bias
bias = 3

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias 
print(output)