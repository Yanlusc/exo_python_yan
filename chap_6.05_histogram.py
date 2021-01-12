def histogram(s):
    """Renvoie le dictionnaire des lettres dans s avec leur fréquence."""
    d = {}   # dictionnaire vide
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print(histogram("blabla"))