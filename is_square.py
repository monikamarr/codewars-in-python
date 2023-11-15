def is_square(n):    
    for i in range(n//2+1):
        if i * i == n:
            return True
    return False
        
