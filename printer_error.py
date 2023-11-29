def printer_error(s):
    s = s.lower()
    count = 0
    for char in s:
        if not correct_char(char):
            count += 1
    return f"{count}/{len(s)}"
            

def correct_char(char):
    if ord(char) >= 97 and ord(char) <= 109:
        return True
    else:
        return False
