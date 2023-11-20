def duplicate_encode(word):
    hm = {}
    new = ""
    word = word.lower()
    for char in word:
        if char in hm:
            hm[char] += 1
        else:
            hm[char] = 1
    for items in word:
        if hm[items] > 1:
            new += ")"
        else:
            new += "("
    return new
