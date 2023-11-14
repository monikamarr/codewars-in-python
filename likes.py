def likes(names):
    if len(names) == 0:
        return "no one likes this"
    for name in range(len(names)):
        if len(names) == 1:
            return f"{names[name]} likes this"
        elif len(names) == 2:
            return f"{names[name]} and {names[name+1]} like this"
        elif len(names) == 3:
            return f"{names[name]}, {names[name+1]} and {names[name+2]} like this"
        else:
            return f"{names[name]}, {names[name+1]} and {len(names) - 2} others like this"
