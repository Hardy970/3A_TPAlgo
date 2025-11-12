def ValAbsolue(n):
    if n < 0:
        return n - (n*2)
    return n
def nImpair(n):
    return n%2 !=0

def prodMod(n,p,m):
    return (n*p)%m

def kDivN(k,n):
    #return k!=0
    if k !=0:
        return n/k
    return None

