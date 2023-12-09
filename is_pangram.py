def is_pangram(s):
    alph = {}
    for i in range(ord('a'), ord('z') + 1):
        alph[chr(i)] = 1
    string = {}
    s = s.lower()
    for char in s:
        if ord(char) < 97 or ord(char) > 122:
            continue
        if char in string:
            string[char] += 1
        else:
            string[char] = 1
    
    return alph.keys() == string.keys()
    
