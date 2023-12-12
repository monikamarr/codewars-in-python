def capitals(word):
    i = []
    for char in range(len(word)):
        if ord(word[char]) >= 65  and ord(word[char]) <= 90:
            i.append(char)
    return i
