print("transfert toutes les données d'un fichier d'entrée dans un fichier de sortie à l'exception des e  ")
f_in = input(" nom du fichier d'entrée")
f_out = input("nom du fichier de sortie")

with open(f_out,"w", encoding ="utf-8") as r:
    deja_vu= set({})
    for text in open("words.txt",encoding="utf-8"):
        for c in text:
            if  c != "e":
                deja_vu |= {text}
                r.write(c)