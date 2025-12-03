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



if __name__ == '__main__':

    wordhb = {}
    wordhp = {}

    mots=readfile("data/mots.txt")


