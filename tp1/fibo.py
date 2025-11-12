from decorators import trace

#@trace
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

"""for i in range(100):
    print(fibo(i))"""
#fibo(13)
# cout en nombre d'addition T(n)= 1 + T(n-1) + T(n-2)
def fibo_norec(n):
    if n < 2 :
        return n
    else:
        p=1
        pp=0
        c=0
        for i in range(1,n):
            c= p+pp
            pp=p
            p=c
        return c
# cout : n
"""for i in range(100):
    print(fibo_norec(i))"""
# 0 1 1 2 3 5 8 13

def fibo_term(n):
    def fibo_aux(m,d):
        if m not in d:
            d[m]= fibo_aux(m-2,d) + fibo_aux(m-1,d)
            return d[m]
        else:
            return d[m]
    return fibo_aux(n,{0:0,1:1})


# a revoir
def fibo_term2(n):
    def fibo_aux2(m,c,acc1,acc2):
        if m < 2:
            return m
        else:
            if c==m:
                return acc2
            return fibo_aux2(m,c+1,acc2,acc1+acc2)
    return fibo_aux2(n,1,0,1)
print(fibo_term2(13))
for i in range(100):
    print(fibo_norec(i))