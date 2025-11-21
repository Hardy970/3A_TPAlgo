def insertionsort(seq: list[int]) -> list[int]:
    for i in range(0,len(seq)-1):
        k = i
        j=i+1
        t = seq[j]
        while k >=0 and seq[k]> t:
            seq[j]= seq[k]
            j-=1
            k-=1
        seq[j]=t
    return seq
    """for i in range(len(seq)):
        min=seq[i]
        for j in range(i,len(seq)):
            if(seq[i]<min)"""

