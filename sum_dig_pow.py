def sum_dig_pow(a, b):
    str_list = []
    to_str = []
    for i in range(a, b + 1):
        if 0 <= i <= 9:
            str_list.append(i)
        else:
            to_str.append(str(i))

    sumi = 0
    squared = 0
    for item in to_str:
        sumi = 0
        for i in range(len(item)):
            squared = int(item[i]) ** (i + 1)
            sumi += squared
        if sumi == int(item):
            str_list.append(sumi)
    return str_list
