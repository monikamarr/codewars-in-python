def are_you_playing_banjo(name):
    name_char = name[0]
    return name + " plays banjo" if name_char == "r" or name_char == "R" else name + " does not play banjo"