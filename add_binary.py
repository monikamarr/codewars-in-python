def add_binary(a, b):
    new = a + b
    remainder = []
    final = ""
    while new >= 1:
        remainder.append(new % 2)
        new //= 2
        
    rev = remainder[::-1]
    
    for i in rev:
        final += str(i)
        
    return final
