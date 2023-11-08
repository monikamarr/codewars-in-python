def solution(s):
    new = ""
    for char in s:
        if uppercase(char):
            char = " " + char 
            new += char
        else: 
            new += char 
    return new
def uppercase(char):
    if ord(char) >= 65 and ord(char) <= 90:
        return True

