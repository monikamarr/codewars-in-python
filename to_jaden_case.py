def to_jaden_case(string):
    string = string.capitalize()
    new_str = ""
    for char in range(len(string)):
        if string[char-1] == " ":
            new_str += string[char].upper()
        else:
            new_str += string[char]
    return new_str
