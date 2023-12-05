def binary_array_to_number(arr):
    new = []
    for i in range(len(arr) -1, -1, -1):
        new.append(arr[i])
    dec = 0
    for i in range(len(new)):
        dec += new[i] * (2 ** i)
    return dec
