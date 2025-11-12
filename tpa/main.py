"""from collatz import * # import et définition (optionnelle) d'alias

seed: int = 1999
index: int = collatz_lifetime(seed)
series: list[int] = collatz_series(seed, index)
height: int = collatz_altitude(seed)
print(f"La suite de Collatz pour N={seed} "f"a une durée de vie de {index}, une altitude de {height}\n"
f"et ses premiers termes sont {series[:10]}") """
from operator import itemgetter

# exercice 3 tpB

#q1
"""Point = tuple[float,float]
def distance_et_barycentre(A: Point, B: Point) -> tuple[float, Point] :
    return A,B
"""
#q2
"""d:dict[int,int]={}
for i in range(100):
    d[i]=i**2

print(d)"""

#q3
"""l1=["Nom","prenom","age"]
l2=["ADIMOU","hardy",20]

d={}
for i in range(len(l1)):
    d[l1[i]]= l2[i]

print(d)"""

#q4

"""d: dict[str,int]={"hardy": 20,"Léo": 14,"Bob":10}
s,c=0,0
for k,v in d.items():
    if k!="Léo":
        s+=d[k]
        c+=1
print(f"Moyenne = {s/c}") """

#q5

"""d: dict[str,int]={"hardy": 13,"Léo": 20,"Bob":10}

l=list(d.items())
print(l)
l.sort(key=itemgetter(1),reverse=True)
for e in l :
    print(e[0])
"""

#q6

"""acid_amine: set[str]
seq = "aucucggucgaccgcgcuuucaucgucggcaaagucaagaucccg"
for(i in range())"""






