def count_digits(n: int, base: int = 10) -> int:
    def count_digits_aux(n,base,c):
        if n==0:
            return c
        return count_digits_aux(n//base,base,c+1)

    return count_digits_aux(n,base,0)

print(count_digits(255,2))