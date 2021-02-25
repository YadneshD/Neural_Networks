print("Enter the four Bipolar inputs and target values in the order")
print("x1 x2 y")
input_array = []
for i in range(4):
    input_array.append([int(x) for x in input().split()])
    
weights = [0,0]
bias = 0
def hebbian(arr):
    global weights, bias
    for i in range(2):
        weights[i] += arr[i]*arr[2]
    bias += arr[2]
i = 1
for arr in input_array:
    hebbian(arr)
    print("for input",i,"the weight w1 =",weights[0],"w2 =", weights[1],"bias =",bias)
    i += 1
