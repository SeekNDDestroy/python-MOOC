word = input("Please type in a word:")
char = input("Please type in a character:")

indexFound = word.find(char)

if indexFound >= 0:
    if indexFound + 3 < len(word):
        print(word[indexFound: indexFound + 3])
