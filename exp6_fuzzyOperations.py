#exp6_fuzzyOperations.py
'''
Name - Yadnesh Dhanawade, Roll no. - 7864,
Problem Statement - Given two fuzzy sets, perform operations on them like union, intersection, complement
difference.
'''

print("Enter the operation you want to perform")
print("1-Complement\n2-Union\n3-Intersection\n4-Difference")
op = int(input())

def complement(A):
    ans = []
    for i in A:
        ans.append(1-i)
    return ans
    
def union(A,B):
    ans = []
    for i in range(len(A)):
        ans.append(max(A[i], B[i]))
    return ans

def intersection(A,B):
    ans = []
    for i in range(len(A)):
        ans.append(min(A[i], B[i]))
    return ans

def difference(A,B):
    B = complement(B)
    ans = intersection(A,B)
    return ans

if op == 1:
    print("Enter the set A")
    A = list(map(float, input().split()))
    print("complement of A =", complement(A))
else:
    print("Enter set A")
    A = list(map(float, input().split()))
    print("Enter set B")
    B = list(map(float, input().split()))
    if op == 2:
        print("AuB =", union(A,B))
    elif op == 3:
        print("AnB =", intersection(A,B))
    elif op == 4:
        print("A-B =", difference(A,B))
    else:
        print("Invalid option selected")