# def func():
#     func()
# func()
# this will give error has the function is being called within itself without a "break"

# Factorial
# Iterative Code
# def factorial(n):
#     fac=1
#     for i in range(1,n+1):
#         fac=fac*i
#     return fac
# print(factorial(6))

# Recursive Code
# def fact(n):
#     if(n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))
#Recursion uses stack

# Fibonacci Series
def iterative_fib(n):
    count=0
    while count<n:
        a,b=0,1
        c=a+b
        b=a
        c=b
        count+=1
    print(c)
iterative_fib(5)


def recursive_fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return recursive_fib(n-1)+recursive_fib(n-2)
print(recursive_fib(3))
