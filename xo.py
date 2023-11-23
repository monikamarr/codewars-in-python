def xo(s):
    count = {}
    s = s.lower()
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1

    if "x" in count and "o" in count:
        count_x = count["x"]
        count_o = count["o"]
        if (count_x == count_o):
            return True
    elif "x" not in count and "o" not in count:
        return True
        
    return False
