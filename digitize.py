def digitize(n):
    """Given a random non-negative number, return the digits
    of this number within an array in reverse order."""
    arr = []
    for i in str(n):
        arr.append(int(i))

    arr.reverse()
    return arr