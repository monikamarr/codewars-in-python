def str_count(strng, letter):
    count = 0
    for char in strng:
        if char == letter:
            count += 1
    return count
