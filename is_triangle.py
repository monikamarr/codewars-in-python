def is_triangle(a, b, c):
    for i in [a,b,c]:
        if i < 0:
            return False
    if (a + b) > c and (a + c) > b and (c + b) > a:
        return True
    return False
