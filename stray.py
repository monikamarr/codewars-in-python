def stray(arr):
    items = {}
    for i in arr:
        if i in items:
            items[i] += 1
        else:
            items[i] = 1
    for key in items:
        if items[key] == 1:
            return key
            
