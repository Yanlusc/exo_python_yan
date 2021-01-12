import turtle
for i in range(3):  # à chaque itération, trace un losange
   angle = 120
   for j in range(4): # à chaque itération, trace un segment
       turtle.forward(100)
       turtle.left(angle)
       angle = 180 - angle
   turtle.right(120)
turtle.hideturtle()
"""
CODE D’UN PAVÉ HEXAGONAL AVEC DES FOR IMBRIQUÉS
Un exemple beaucoup plus difficile à ce stade de votre apprentissage, est d’écrire un code qui utilise turtle pour faire un pavé hexagonal tel que demandé au module précédent, mais en ayant le code le plus succinct possible grâce à l’utilisation d’instructions for.

Pavé coloré

Pavé coloré

En effet, on peut constater qu’un tel pavé est constitué de 3 losanges, chacun constitué de 4 côtés de même taille, mais reliés avec des angles alternativement de 60° ou de 120°.

Comme nous n’avons pas encore vu la notion de séquence qui nous aidera pour faire l’exemple complet, essayez d’écrire le code qui utilise en particulier des instructions for pour tracer l’ensemble des lignes de l’hexagone, mais sans changer de couleur ni remplir les surfaces, tel que montré ici:

Pavé non coloré

Pavé non coloré

Aide: on peut voir que le code suivant imprime 4 fois la valeur d’une variable angle en alternant entre les deux valeurs 120 et 60 (120, 60, 120, 60). En effet ce code utilise le fait que 180 - 120 vaut 60 et 180 - 60 vaut 120.

angle = 120
for j in range(4):
       print(angle)
       angle = 180 - angle
Par ailleurs,

le premier losange commence son tracé par un segment de ligne horizontal,
le second, par un segment qui forme un angle de 120° par rapport au premier segment,
le troisième, par un segment qui forme un angle de 120° par rapport au second segment.
En résumé, il faut répéter trois fois:

tracer un losange (où à chaque fois il faut tracer 4 segments)
ensuite tourner à droite de 120°
Le caneva général sera donc :
"""