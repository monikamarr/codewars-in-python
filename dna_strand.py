def DNA_strand(dna):
    new = ""
    for char in dna:
        if char == "A":
            char = "T"
        elif char == "T":
            char = "A"
        elif char == "G":
            char = "C"
        elif char == "C":
            char = "G"
            
        new += char
    return new
