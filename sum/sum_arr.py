def sum_array(arr):
    if arr is None or arr == []:
        return 0
    arr.sort()
    sum = 0
    new = arr[1:len(arr)-1]
    for i in range(len(new)):
        sum += new[i]
    return sum
