def nb_year(p0, percent, aug, p):
    percent /= 100
    n = 0
    while p0 < p:
        p0 = int(p0 + (p0 * percent) + aug)
        n += 1
    return n 
