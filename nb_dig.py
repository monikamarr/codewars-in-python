def nb_dig(n, d):
    new = []
    count = 0
    for k in range(n+1):
        k **= 2
        new.append(str(k))
    for num in new:
        for digit in num:
            if d == int(digit):
                count += 1
    return count
