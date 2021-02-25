print("Enter number of rows in matrix A")
arows = int(input())
print("Enter number of rows in matrix B")
brows = int(input())

amatrix = []
print("Enter matrix A")
for i in range(arows):
    amatrix.append(list(map(float, input().split())))
bmatrix = []
print("Enter matrix B")
for i in range(brows):
    bmatrix.append(list(map(float, input().split())))

temp1 = []
flag1 = True
answer = []
for i in range(brows):
    temp2 = []
    for j in range(len(bmatrix)):
        temp2.append(min(amatrix[i][j], bmatrix[j][i]))
    temp1.append(max(temp2))
    if len(temp1) == len(amatrix[0]):
        answer.append(temp1)
        temp1 = []
print("Final answer is")
for i in range(brows):
    print(answer[i])

    
