def func1(x1, x2):
    print("*******************")
    print("Binary inputs x1 and x2 given are x1 =", x1,"and x2 =",x2)
    if x1 in [0,1] and x2 in [0,1]:
        pass
    else:
        return "Invalid Inputs given"
    summ = x1 + x2
    if summ >= 2:
        return "Nueron is fired for AND gate"
    else:
        return "Nueron is not fired for AND gate" 
    
print(func1(0,0))
print(func1(1,0))
print(func1(0,1))
print(func1(1,1))
print(func1(3,1))