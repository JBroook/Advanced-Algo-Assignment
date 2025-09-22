import sys

def factorial1(n):
    if n==2:
        return 2
    return n*factorial1(n-1)

def factorial(n):
    res = 1
    while n>1:
        res *= n
        n -= 1
    return res

if __name__=="__main__":
    print(factorial(1001))
    print(sys.getrecursionlimit())