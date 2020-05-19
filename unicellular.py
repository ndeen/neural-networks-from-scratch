# the first neuron

# these inputs represent outputs from the previous layer
inputs = [1.0, 2.0, 3.0, 2.5]

# each unique input has a unique weight associated with it
weights = [0.2, 0.8, -0.5, 1.0]

# each neuron has its own bias
bias = 2.0

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] + bias

print(output)