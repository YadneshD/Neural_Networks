# python pattern_classifier_perceptron.py
'''
ALGORITHM - 
1- The input patterns are taken. 1 for '*' and -1 for '.'
2- The target value ta =1 and tb = -1 for pattern a and pattern b respectively.
3- pattern_a and pattern_b are the lists that contain the Xi values for pattern a and pattern b.
3- weightchanger is the function which changes the weights and bias according to target value.
It takes target, pattern, weights, bias as arguments.
4- The program will go on changing weights until Yin != target for both input patterns

WORKING of weightchanger- 
1- first it calculates the Yin value by adding bias and computing sum of Xi*Wi of pattern and weights lists respectively
2- if Yin(summ) == target then it returns weights list as it is else it goes on step 3.
3- new value of each element of weight list = old value + target*Xi (because alpha is assumed to be one)
4- returns weights list, bias and a boolean flag value which says if there are any changes in weights or not.
'''
print("Pattern classifier using PERCEPTRON LEARNING RULE")
print("The index pattern is")
print("1 2 3")
print("4 5 6")
print("7 8 9")
def main():
    print("In pattern 1(target value = 1), enter the indices for which values are '1', for remaining indices '-1' value will be assumed")
    a = [int(a) for a in input().split()]
    print(a)
    print("Similarly, Enter indices for pattern 2(target value = -1)")
    b = [int(b) for b in input().split()]
    print(b)    

    def weightchanger(target, pattern, weights, bias):
        yin = 0
        flag = False
        yin += bias
        for i in range(9):
            yin += pattern[i]*weights[i] # Xi*Wi
        if yin >0:
            y = 1
        elif yin<0:
            y = -1
        else:
            y = 0
        
        if y == target:
            flag = True
        else:
            for i in range(9):
                weights[i] = weights[i] + target*pattern[i]
            bias = bias + target
        return bias, weights, flag
    
    pattern_a = [-1 for i in range(9)]
    pattern_b = [-1 for i in range(9)]
    for i in a:
        pattern_a[i-1] = 1
    for i in b:
        pattern_b[i-1] = 1
    
    ta, tb = 1, -1
    bias = 0
    weights = [0 for i in range(9)]
    epoch =1
    while True:
        inputflags = [False, False]
        bias, weights, inputflags[0] =  weightchanger(ta, pattern_a, weights, bias)
        bias, weights, inputflags[1] = weightchanger(tb, pattern_b, weights, bias)
        print("After",epoch,"epoch the bias and weights are-")
        print("bias =",bias,"weights = ", weights)         
        if inputflags == [True, True]:
            break
        epoch += 1
    print("Final weights and bias are")
    print("b = ", bias,"weights = ", weights)

main()