def power(a: int, n: int) -> int:
    if n==1:
        return a
    elif n == 0:
        return 1
    else:
        return power(a,n//2)*power(a,(n+1)//2)


#print(power(2,2))

def superpower(a: int, n: int) -> int:
    if n==1:
        return a
    else:
        if n%2 ==0:
            return superpower(a,(n//2))*superpower(a,(n//2))
        else:
            return superpower(a,(n//2))*superpower(a,(n//2)+1)

#print(superpower(2,2))
