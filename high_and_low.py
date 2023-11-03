def high_and_low(numbers):
    new = numbers.split()
    
    for char in range(len(new)):
        new[char] = int(new[char])
        
    mini = min(new)
    maxi = max(new)
    numbers = (f"{maxi} {mini}")
    
    
    return numbers
