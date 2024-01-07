def count_smileys(arr):
    smiles = [":)", ":D", ";)", ";D"]
    nose = [":-)", ":-D", ";-)", ";-D", ":~)", ":~D", ";~)", ";~D"]
    count = 0
    for face in arr:
        if len(face) < 2 or len(face) > 3:
                continue
        if face in smiles or face in nose:
            count += 1
    return count
