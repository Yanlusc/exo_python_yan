s = {'a', 'b', 'c', 'd', 'e'}
for i in s:
    if i in 'aeiouy':
        s.remove(i)
"""
Traceback (most recent call last):
  File "<input>", line 1, in <module>
RuntimeError: Set changed size during iteration
"""

list(set(s)& set("aeiouy"))
list(set("pommeee") & set("banane")) #liste des lettres communes ['e']
#code qui marche

