from functools import  cache
@cache
def binom(n: int, k: int) -> int:
    if k  ==0 or k==n:
        return 1
    else:
        return binom(n-1,k-1) + binom(n-1,k)

print(binom(5,3))
print(binom(10,5))
print(binom(42,1))
print(binom(100, 50))

def binom_mem(n: int, k: int) -> int:
    def binommem_aux(n:int,k:int,acc:dict):
        if (n,k) in acc:
            return acc[(n,k)]
        else:
            if k == 0 or k == n:
                acc[(n,k)]=1
                return acc[(n,k)]
            else:
                acc[(n,k)] =binommem_aux(n - 1, k - 1,acc) + binommem_aux(n - 1, k,acc)
                return acc[(n,k)]

    return binommem_aux(n,k,{(1,0): 1,(1,1):1})
"""print(binom_mem(5,3))
print(binom_mem(10,5))
print(binom_mem(42,1))
print(binom_mem(100, 50))"""