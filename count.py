def count(s):
    if len(s) == 0:
        return {}
    else:
        hmap = {}
        for char in s:
            if char in hmap:
                hmap[char] += 1
            else:
                hmap[char] = 1
        return hmap
