def min_max(lst):
    new_list = []
    maxi = lst[0]
    mini = lst[0]
    for i in lst:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
    return [mini, maxi]
