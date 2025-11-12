def collatz_altitude(seed):

    max_value = seed
    equal_to_one = 1 # end condition

    while seed != equal_to_one:
        if seed %2 == 0:
            seed = seed // 2

            if seed > max_value:
                max_value = seed
            else:
                pass

        else:
            seed = 3 * seed + 1

            if seed > max_value:
                max_value = seed
            else:
                pass

    #print(seed)
    return max_value

def collatz_lifetime(seed):
    count = 0
    equal_to_one = 1
    while seed != equal_to_one:
        if seed %2 == 0:
            seed = seed // 2
            count += 1
        else:
            seed = 3 * seed + 1
            count += 1
    return count

def collatz_series(u0,N):
    res = [u0]
    for i in range(N):
        if u0 % 2 == 0:
            u0 = u0 // 2
            res.append(u0)
        else:
            u0 = 3 * u0 + 1
            res.append(u0)
    return res

if __name__ == "__main__":
    print(collatz_series(7, 10))