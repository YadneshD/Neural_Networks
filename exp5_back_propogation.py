# python exp5_back_propogation.py
from math import exp

def binary_sigmoidal(n):
    return 1/(1+exp(-n))

print("Back-Propogation network with binary sigmoidal activation function")  
n = 2
print("Enter number of epochs")
total_epochs = int(input())
print("Enter the inputs")
ip_pattern = list(map(float, input().split()))
print("Enter learning rate, alpha")
alpha = float(input())
print("Enter target output d")
d = float(input())

biases = []
input_weights = []
for i in range(1,n+1):
    list1 = []
    for j in range(1,n+1):
        print("Enter the weight v"+str(i)+str(j))
        Wij = float(input())
        list1.append(Wij)
    input_weights.append(list1)
    print("Enter the bias for v0"+str(i),"nueron of hidden layer")
    biases.append(float(input()))
hidden_weights = []
for i in range(n):
    print("Enter the weight w"+str(i+1),"(from hidden layer nueron to output nueron)")
    hidden_weights.append(float(input()))
print("Enter the bias for last nueron i.e w0")
last_bias = float(input())

def main_calculator(input_weights, biases, last_bias, hidden_weights):
    global n, ip_pattern,d
    Zin_array = []
    for i in range(n):
        zin = biases[i]
        for j in range(n):
            zin += input_weights[j][i]*ip_pattern[j]
        Zin_array.append(zin)
    
    fZin_array = []
    for i in range(n):
        fZin_array.append(binary_sigmoidal(Zin_array[i]))
    #print("fZin_array =",fZin_array)
    yin = last_bias
    for i in range(n):
        yin += fZin_array[i]*hidden_weights[i]
    #print("Yin =",yin)
    y = binary_sigmoidal(yin)
    derivative_y = y*(1-y)
    delta1 = derivative_y*(d-y)
    #print("delta1 =", delta1)
    new_hidden_weights = []
    for i in range(n):
        new_hidden_weights.append(alpha*delta1*fZin_array[i] + hidden_weights[i])
    new_last_bias = last_bias + alpha*delta1
    
    delta_in = []
    for i in range(n):
        delta_in.append(delta1*hidden_weights[i])
    
    errors = []
    for i in range(n):
        x = delta_in[i]*fZin_array[i]*(1 - fZin_array[i])
        errors.append(x)
    #print(delta_in, errors)
    new_biases = []
    new_input_weights = []
    for i in range(n):
        xxx = []
        for j in range(n):
            x = input_weights[i][j] + alpha*errors[j]*ip_pattern[i]
            xxx.append(x)
        new_input_weights.append(xxx)
        new_biases.append(biases[i] + alpha*errors[i])
    #print(new_input_weights, new_biases, new_last_bias, new_hidden_weights)
    return new_input_weights, new_biases, new_last_bias, new_hidden_weights

for xx in range(1, total_epochs+1):
    input_weights, biases, last_bias, hidden_weights = main_calculator(input_weights, biases, last_bias, hidden_weights)
    #print(input_weights, biases, last_bias, hidden_weights)
    print("********************************************************")
    print("In epoch", xx, "the biases for hidden layer were calculated as")
    for i in range(0,n):
        print("bias v0"+str(i+1), "=", biases[i])
    print("The bias for last nueron, w0 =", last_bias)
    for i in range(n):
        for j in range(n):
            print("v"+str(i+1)+str(j+1), "=", input_weights[i][j])
    for i in range(n):
        print("w"+str(i+1), "=", hidden_weights[i])

