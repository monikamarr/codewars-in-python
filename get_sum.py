def get_sum(a, b):
    """Given two integers a and b, which can be positive or negative,
    find the sum of all the integers between and including them and
    return it. If the two numbers are equal return a or b.

    Note: a and b are not ordered!"""
    if a == b:
        return a
    else:
        sum = 0
        if a > b:
            for i in range(b, a + 1):
                sum += i

        for i in range(a, b + 1):
            sum += i
        return sum
