x = 5

def fib(n):
    result = []
    a, b = 0,1
    while b<n:
        result.append(b)
        a,b = b, a+b
    return result

def mytest(a,b):
    global x
    x = a +b

mytest(3,5)
print(x)

f = fib(100)
print(f)

import math
content = dir(math)
print(content)