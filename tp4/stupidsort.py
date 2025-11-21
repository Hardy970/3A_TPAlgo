import random
from os import MFD_ALLOW_SEALING


def stupidsort(seq: list[int]) -> list[int]:
    trier=False
    while not trier:
        random.shuffle(seq)
        fin=False
        i=0
        while not fin and i<len(seq)-1:
            if seq[i] > seq[i + 1]:
                fin=True
            i+=1
        if i==len(seq)-1 and fin==False:
            trier= True
    return seq

print(stupidsort([9,56,1,789,0,61,-12,567,90]))
