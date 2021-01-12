voyelles = "aeiouy"
x = list(enumerate('bonjour'))
for i in range(len(x)):
    if x[i][1] in voyelles:
        del x[i]