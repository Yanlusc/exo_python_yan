with open('mots.txt') as f:
    print([w.strip() for w in f if {'a','e','i','o','u','y'} <= set(w)])