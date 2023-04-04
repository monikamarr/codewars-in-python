def filter_list(l):
    """return a new list with the strings filtered out"""
    new_arr = []
    for item in l:
        if isinstance(item, int):
            new_arr.append(item)


    return new_arr