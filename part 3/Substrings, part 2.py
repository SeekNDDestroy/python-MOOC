word = input("Please type in a string:")
i = len(word)

while i > 0:
    print(word[i-1:])
    i -= 1