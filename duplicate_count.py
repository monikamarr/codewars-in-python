def duplicate_count(text):
    text = text.lower()
    hashmap = {}
    for char in text:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1
    count = 0
    for key in hashmap:
        if hashmap[key] > 1:
            count += 1
    return count
