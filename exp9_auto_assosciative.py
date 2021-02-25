import numpy as np
def transposeandmultiplier(x):
    y = []
    for i in range(len(x)):
        temp = []
        for j in range(len(x)):
            temp.append(x[i]*x[j])
        y.append(temp)
    return np.array(y)
    
print("Enter the number of vectors to be stored")
n = int(input())
print("Enter vector 1")
x = list(map(int, input().split()))
weightmatrix = transposeandmultiplier(x)
for i in range(1,n):
    print("Enter vector", i+1)
    x = list(map(int, input().split()))
    weightmatrix += transposeandmultiplier(x)
print("Final weight matrix is")
print(weightmatrix)