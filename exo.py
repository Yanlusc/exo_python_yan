def anagramme_str1(a, b):
    res = False
    for i in a:
        res = (i in b)
    return res
la="la"
al="al2"
anagramme_str1 (la,al)