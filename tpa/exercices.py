import math

"""xa,xb,ya,yb = 2,5,7,3
print('la distance entre A et B est',( (xb - xa)**2 +(yb-ya)**2 )**(1/2))"""

#Exercice 5
#question 1
"""var = 18 
if var % 2 == 0:
    if var % 3 ==0:
        print("pair et divisible par 3")
    else:
        print("pair et non divisible par 3")

else :
    print("impair") """

#question 3

"""for i  in range (10):
    print(i)"""

#question 4
"""
for i in range(0,10,2):
    print(i)
"""

# question 5
"""for i in range(10,0,-2):
    print(i)"""

# question 6
"""for i in range(0,100):
    if (i % 2 == 0) or (i % 3 == 0):
        print(i**3)"""

# question 7

"""a = 5
b = 7
while(a<b):
    print(a)
    a+=1"""


# question 8

"""b = 10
while(b>=0):
    if b % 2 != 0:
        print(b)
    b-=1"""


# Exercice 6

#question 1

"""cubes_nombres = [i**3 for i in range(100)]
print(cubes_nombres)"""

#question 2

"""cubes_nombre_pair = [i**3 for i in range(100) if i % 2 == 0]
print(cubes_nombre_pair)"""

#question 3

"""cubes_nombre_pair2 = [i**3 for i in range(99,-1,-1) if i % 2 == 0]
print(cubes_nombre_pair2)"""


# question 4
"""nombres = [1, 5, 42, 1 ,9]
carrés = [i ** 2 for i in range(10)]"""

"""nombres_carré = [ i for i in nombres if math.sqrt(i) >=2 and math.sqrt(i) <=4]
print(nombres_carré)"""

#question 5


"""nombres_carré = [ i*2 if i%3 != 0 else 0 for i in nombres if math.sqrt(i) >=2 and math.sqrt(i) <=4]
print(nombres_carré)"""



#Exercice 7

#question 1

"""nombres.sort()
print(nombres)"""

#question 2

"""nombres.append(-42)
print(nombres)"""

#question 3

"""nombres.reverse()
print(nombres)"""

#question 4
"""nombres.remove(5)
print(nombres)"""

#question 5
"""print(nombres.index(42))"""

#questtion 6
"""carrés = carrés + nombres
print(carrés)"""

#question 7
"""print(nombres[1:3])"""

#question 8
"""print(nombres[:3])"""

#question 9
"""print(nombres[2:])"""

#question 10
"""print(nombres[-1])"""

#Exercice 8

"""n = 3
heroes = "mousquetaires"
print(f"Les {n} {heroes} étaient {n+1} en réalité")
print(f"{14 * n = } et les f-strings sont formidables !")"""

#q1

word="Bienvenue"
"""
print(len(word),word[0],word[-1])"""

#q2

#print(word.upper(),word.lower())

#q3
greeting= "Bonjour"
to="le monde!"
sentence= greeting +" " +to
#print(sentence)

#q4
#print(sentence.index("monde"),sentence.count("on"))

#q5
"""sentence2= sentence.replace("le monde","Hardy")
print(sentence2)"""

#q6

"""seq=""
for i in range(100):
    seq+="AGTCAG"

print(seq) """

#q7

