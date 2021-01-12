

def factorial(n):
    if n < 1: # base case
        return 1
    else:
        result = n * factorial(n - 1)
        return result

def fibonachi(x):
    z = True
    n = 0
    while z:
        n = n+1
        y=x
        x = x + fibonachi((-1**(n+2)*x**(n+2))/(factorial(2*n+1)))
        if (x-y)<(10**(-6)): 
            z = not z
            return x

fibonachi(0,707106781)