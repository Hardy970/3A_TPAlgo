from tp2.util import StaticArray, alloc,nops,reset_nops,random_array,array_to_list,list_to_array
def mode(tab: StaticArray) -> int:
    d={}
    for i in range(len(tab)):
        e=tab[i]
        if e in d:
            d[e]+=1
        else:
            d[e]=1
    maxi=0
    for e in d:
        if d[e] > maxi:
            maxi=e
    return maxi

"""tab: StaticArray= random_array(10,1,5)
print(tab)
print(mode(tab))
print(nops(tab))"""

def cumulative_sum(tab: StaticArray) -> StaticArray:
    tab2: StaticArray= alloc(len(tab))
    s=0
    for i in range(len(tab)):
        for j in range(i+1):
            s+=tab[j]
        tab2[i]=s
        s=0

    return tab2

"""tab: StaticArray= random_array(10,1,100)
print(tab)
print(cumulative_sum(tab))"""

def duplicate_elimination(tab: StaticArray) -> StaticArray:
    listeSansDoublon: StaticArray= alloc(len(tab))
    nombreElementLSD=0
    for i in range(len(tab)):
        b=0
        for j in range(nombreElementLSD):
            if listeSansDoublon[j]==tab[i]:
                b=1
                break
        if b ==0:
            listeSansDoublon[nombreElementLSD]=tab[i]
            nombreElementLSD+=1
    l:StaticArray= alloc(nombreElementLSD)
    for i in range(nombreElementLSD):
        l[i]=listeSansDoublon[i]
    return l

"""tab: StaticArray= random_array(10,1,5)
print(tab)
print(duplicate_elimination(tab))"""

def binary_search(tab: StaticArray, x: int) -> int:
    a,b=0,len(tab)
    while a<b:
        m = (int)(a + b / 2)
        if tab[m]==x:
            return m
        if tab[m] > x:
            b=m-1
        if tab[m] < x:
            a=m+1
    return -1


tab: StaticArray= random_array(10,1,5)
print(sorted(array_to_list(tab)))
d=list_to_array(array_to_list(tab))
print(binary_search(d,1))







