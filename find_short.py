def find_short(s):
    s = s.split()
    min = len(s[0])
    for word in s:
        if len(word) < min:
            min = len(word)
    return min
