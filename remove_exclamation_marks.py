def remove_exclamation_marks(s):
    """if exclamation mark in a string, remove it"""
    if "!" in s:
        s = s.replace("!","")
    return s
