numbers: list[int] = [k for k in range(1_000)]

"""for i in range(len(numbers)):
    if not bool(numbers[i] % 2):
        del numbers[i]
    else:
        numbers[i] = numbers[i] * i
print(numbers)"""

for i,e in enumerate(numbers):
    if not bool(e % 2):
        del e
    else:
        e = e * i
print(numbers)