def reverse_letter(string):
    rev = string[::-1]
    new = ""
    for char in rev:
        if char >= 'a' and char <= 'z':
            new += char
    return new
    


    
