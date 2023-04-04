def descending_order(num):
    """a function that can take any non-negative
    integer as an argument and return it with its
    digits in descending order."""
    string = str(num)
    new_list = []
    for char in string:
        new_list.append(int(char))
    new_list.sort()
    new_list.reverse()
    l = []
    for item in new_list:
        str_item = str(item)
        l.append(str_item)
    final = "".join(l)
    return int(final)