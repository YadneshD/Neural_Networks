print("Enter the four Bipolar inputs and target values in the order")
print("x1 x2 y")
input_array = []
for i in range(4):
    input_array.append([int(x) for x in input().split()])
    
weights = [0,0]
bias = 0

def biasweightchanger(inputs, weights, bias):
    target = inputs[2]
    yin = 0
    flag = False
    yin += bias
    for i in range(2):
        yin += inputs[i]*weights[i] # Yin = Yin + Xi*Wi
    if yin >0:
        y = 1
    elif yin<0:
        y = -1
    else:
        y = 0
    if y == target:
        flag = True
    else:
        for i in range(2):
            weights[i] = weights[i] + target*inputs[i]
        bias = bias + target
    return bias, weights, flag

epoch = 1
while True:
    print("*********************************")
    inputflags = [False, False, False, False]
    bias, weights, inputflags[0] = biasweightchanger(input_array[0], weights, bias)
    print("In epoch",epoch,";input1 weights and bias are", weights,bias)
    bias, weights, inputflags[1] = biasweightchanger(input_array[1], weights, bias)
    print("In epoch",epoch,";input2 weights and bias are", weights,bias)
    bias, weights, inputflags[2] = biasweightchanger(input_array[2], weights, bias)
    print("In epoch",epoch,";input3 weights and bias are", weights,bias)
    bias, weights, inputflags[3] = biasweightchanger(input_array[3], weights, bias)
    print("In epoch",epoch,";input4 weights and bias are", weights,bias)
    if inputflags == [True, True, True, True]:
        break
    epoch += 1
print(epoch,"epochs were taken in total")