import random
secret = random.randint(0, 100)
i = 0
a = int(input("Veuillez entrer un numéro"))

while i < 6:
    i = i+1
    if i == 5:
        print("Perdu ! Le secret était", secret)
    else:
        

        if a == secret:
            print("Gagné en", i, " essais")
        elif (a > secret ):
            print("Trop grand")
        elif (a < secret ):
            print("Trop petit")
  
            
y = int(input("Entrez votre taille "))
while y < 199:
    x = y
    y = y + 2
    
    if x < 20 :
        break
    
    if x == 58 or x == 23:
        continue
    print("Bravo tu as grandi")
    print("Tu as gagne 10 euros")
    

        
    

