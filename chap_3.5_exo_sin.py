fact=1
n=0
x=input('abc ')
x=float(x)
sinx=0
while n>-1:
    if n>=1:
        fact = (2*n+1)*(2*n)*fact
    else:
        fact = 1
    
    inx= (-1)**n*x**(2*n+1)/fact
    sinx= sinx+inx
    if 10**(-6)>abs(inx):
        n=-2
    else:
        n=n+1
    
print(sinx)