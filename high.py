def high(x):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    # assigning the value to each letter
    hm = {}
    for letter in range(len(alphabet)):
        hm[alphabet[letter]] = letter + 1
    print(hm)
    
    # splitting the string into separeate list items
    words = x.split()
    # print(words)
    
    calculated = []
    sum = 0
    i = 0
    # calc sum of each separate string and appending to a new list
    for word in words:
        i += 1
        for letter in word:
            sum += hm[letter]
        calculated.append(sum)
        sum = 0
    
    maxi = max(calculated)
    str_index = calculated.index(maxi)
    return words[str_index]
