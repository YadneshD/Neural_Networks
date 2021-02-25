print("Adaline network using delta rule")
print("Enter the four inputs and target values in the order")
print("x1 x2 y")
input_array = []
for i in range(4):
    input_array.append([int(x) for x in input().split()])

print("Enter initial value of weights w1, w2")
weights = list(map(float,input().split()))
print("Enter initial value of bias")
bias = float(input()) 
print("Enter the learning rate alpha")
alpha = float(input())
print("Enter the number of epochs")
epochs = int(input())

def biasweightchanger(inputs, weights, bias):
    global alpha
    yin = 0
    yin += bias
    for i in range(2):
        yin += inputs[i]*weights[i] # Yin = Yin + Xi*Wi
    t_yin = inputs[2] - yin
    for i in range(2):
        weights[i] +=  alpha*t_yin*inputs[i]
        weights[i] = round(weights[i],4)
    bias = bias + alpha*t_yin
    error = t_yin**2
    return round(bias,4), weights, round(error, 4)

i = 1
while i <= epochs:
    print("*********************************")
    tms_error = 0
    bias, weights, error = biasweightchanger(input_array[0], weights, bias)
    tms_error += error
    print("In epoch",i,";input1 weights and bias are", weights,bias, "error is", error)
    bias, weights, error = biasweightchanger(input_array[1], weights, bias)
    tms_error += error
    print("In epoch",i,";input2 weights and bias are", weights,bias, "error is", error)
    bias, weights, error = biasweightchanger(input_array[2], weights, bias)
    tms_error += error
    print("In epoch",i,";input3 weights and bias are", weights,bias, "error is", error)
    bias, weights, error = biasweightchanger(input_array[3], weights, bias)
    tms_error += error
    print("In epoch",i,";input4 weights and bias are", weights,bias, "error is", error)
    print("At the end of epoch",i,"total mean square error is", tms_error)
    i += 1
