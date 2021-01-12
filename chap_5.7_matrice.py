n=4
m=0
matrice=[[0]*n for i in range(n)]

for i in range(n):
    m+=1
    for j in range (n):
        m+=1
        matrice[i][j] = m
print(matrice)