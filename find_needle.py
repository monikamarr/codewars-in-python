def find_needle(haystack):
    """function takes in an array, finds the "needle"
     and returns its position"""
    for item in range(len(haystack)):
        if haystack[item] == "needle":
            return f"found the needle at position {item}"
