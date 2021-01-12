# pgcd
# règle mathématique symplification le pgcd de x et y est le meme
# le pgcd de y et x Modulo y
# example le pgcd de 132 et 36 est le meme que le pgcd de 36 et 24
# Quand la modulo est égale à 0
# règle mathématique le pgcd de (x,0) est x
x = int(input("Veuillez entrer a:"))
a=x
y = int(input("Veuillez entrer b:"))
b=y
print("Calcule du pgcd")
while y > 0:
    x, y = y, x%y
    print(x,y)
print ("le pgcd de ", a, "et de ",b, " est ",x  )