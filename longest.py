def longest(a1, a2):
    new = {}
    for char in a1:
        new[char] = None

    for char in a2:
        new[char] = None

    return "".join(sorted(new))
        
   
