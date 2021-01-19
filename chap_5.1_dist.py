x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())
def distance_points():
    mon_tuple = x1, y1
    f_tuple = x2, y2
    dist = ((f_tuple[0]-mon_tuple[0])**2 + (f_tuple[1]-mon_tuple[1])**2)**0.5
    return print(dist)
distance_points()