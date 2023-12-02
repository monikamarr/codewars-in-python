def get_middle(s):
    mid = len(s) // 2 
    if len(s) % 2 == 0:
        
        return f"{s[mid-1]}{s[mid]}"
    else:
        return f"{s[mid]}"
