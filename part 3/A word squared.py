def squared(word, times):
    longWord = word * (times * times)
    for i in range(times):
        print(longWord[:times])
        longWord = longWord[times:]



squared("python", 15)