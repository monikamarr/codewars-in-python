def square_digits(num):
    num = str(num)
    ints = 0
    st =""
    for char in range(len(num)):
        ints = int(num[char])
        ints **= 2
        strs = str(ints)
        st += strs
    return int(st)
