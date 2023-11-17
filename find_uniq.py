def find_uniq(arr):
    maxi = max(arr)
    mini = min(arr)
    new_list = []
    for i in range(3):
        new_list.append(arr[i])
    countMax = 0
    countMin = 0
    for i in new_list:
        if maxi == i:
            countMax += 1
        if mini == i:
            countMin += 1
    if countMax > 1:
        return mini
    if countMin > 1:
        return maxi

        
    return n   # n: unique number in the array
