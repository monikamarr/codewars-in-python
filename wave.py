def wave(people):
    wave = []
    word = []
    for i in range(len(people)):
        word.append(people[i])
    for i in range(len(word)):
        if word[i] == " ":
            continue
        word[i] = word[i].upper()
        ready = "".join(word)
        word[i] = word[i].lower()
        wave.append(ready)
    return wave
