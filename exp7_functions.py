print("Enter the type of function.")
print("1-T function\n2-L function\n3-Triangular function\n4-Pie Function\n5-Zadeh function")
option = int(input())

if option == 1:
    print("Enter x, alpha and Beta")
    x, alpha, beta = [float(alpha) for alpha in input().split()]
    if x>= alpha:
        y = 0
    elif x > beta:
        y = 1
    else:
        y = (x-alpha)/(beta-alpha)
    print("Y =", y)
elif option == 2:
    print("Enter x, alpha and Beta")
    x, alpha, beta = [float(alpha) for alpha in input().split()]
    if x<= alpha:
        y = 0
    elif x > beta:
        y = 1
    else:
        y = (x-alpha)/(beta-alpha)
    print("Y =", y)
elif option == 3:
    print("Enter x, alpha, beta and gamma")
    x, alpha, beta, gamma = [float(alpha) for alpha in input().split()]
    if x<= alpha:
        y = 0
    elif x <= beta:
        y = (x-alpha)/(beta-alpha)
    elif x <= gamma:
        y = (gamma - x)/(gamma - beta)
    else:
        y = 0
    print("Y =", y)
elif option == 4:
    print("Enter x, alpha, beta and gamma")
    x, alpha, beta, gamma, delta = [float(alpha) for alpha in input().split()]
    if x<= alpha:
        y = 0
    elif x <= beta:
        y = (x-alpha)/(beta-alpha)
    elif x <= gamma:
        y = 1
    elif x<= delta:
        y = (delta-x)/(delta - gamma)
    else:
        y = 0
    print("Y =", y)
else:
    print("Enter x, alpha, beta and gamma")
    x, alpha, beta, gamma = [float(alpha) for alpha in input().split()]
    if x<= alpha:
        y = 0
    elif x <= beta:
        y = 2*((x-alpha)/(gamma-alpha) ** 2)
    elif x <= gamma:
        y = 1 - 2*((x-alpha)/(gamma-alpha) ** 2)  
    else:
        y = 0
    print("Y =", y)