a=float(input())
b=float(input())
c=float(input())
def  rac_eq_2nd_deg (a,b,c):
    delta= b**2-4*a*c
    racin= delta**0.5
    r3=0

    if delta==0:
        r1 = -b/(2*a)
        mon_tuple = (r3,r1)
    elif delta>0:
        r1 = (-b+racin)/(2*a)
        r2 = (b+racin)/(2*a)
        mon_tuple = (r1,r2)
    else :
        mon_tuple = tuple()
    return (mon_tuple)
rac_eq_2nd_deg(a,b,c)
