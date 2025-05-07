word = input("Please type in a word:")
char = input("Please type in a character:")


newIndex = word.find(char) + len(char)

word = word[newIndex:]
if word.find(char) != -1:
    print("The second occurrence of the substring is at index", str(word.find(char)+newIndex)+".")
else:
    print("The substring does not occur twice in the string.")