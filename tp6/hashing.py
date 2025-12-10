def hashcode_binary(s: str) -> int:
    return int.from_bytes(str.encode(s))
def hashcode_polynomial(s: str) -> int:
    h=0
    for i in range(len(s)):
        h+= ord(s[i])* (31**i)
    return h%(2**64)

def readfile(chemin):
    mots =[]
    with open(chemin,"r",encoding="utf-8") as f :
        for ligne in f:
            mots.append(ligne.strip())
    return mots

def compress_mod(n: int, m: int) -> int:
    return n%m

def compress_mad(n: int, m: int, p: int, a: int, b: int) -> int:
    return (a*n + b)%p%m

if __name__ == '__main__':

    wordhb = {}
    nb_collision=0
    moyenne=0
    nombreTermC=0
    wordhp = {}
    wordh={}

    mots=readfile("data/mots.txt")
    for mot in mots :
        h= hashcode_binary(mot)
        if h not in wordhb:
            wordhb[h] = 1
        elif h in wordhp:
            wordhp[h] += 1

    for v in wordhb.values():
        if v > 1:
            nb_collision+=1

    print(nb_collision)

    nb_collision=0
    for mot in mots :
        h= hash(mot)
        if h not in wordh:
            wordh[h] = 1
        elif h in wordh:
            wordh[h] += 1

    for v in wordh.values():
        if v > 1:
            nb_collision+=1

    print(nb_collision)

    nb_collision = 0
    for mot in mots:
        h = hashcode_polynomial(mot)
        if h not in wordhp:
            wordhp[h] = 1
        elif h in wordhp:
            wordhp[h] += 1

    for v in wordhp.values():
        if v > 1:
            nb_collision += 1

    print(nb_collision)


























