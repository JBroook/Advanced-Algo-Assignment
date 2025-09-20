# def factorial(n):
#     if n==2:
#         return 2
#     return n*factorial(n-1)

def factorial(n):
    res = 1
    while n>1:
        res *= n
        n -= 1
    return n

# print(factorial(6))