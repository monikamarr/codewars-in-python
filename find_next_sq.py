def find_next_square(sq):
    root = sq ** (1/2)
    if root > int(root):
        return -1
    next = root + 1
    return next ** 2
