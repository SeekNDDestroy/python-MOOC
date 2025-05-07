sentence = input("Please type in a sentence:")
sentence += " "
word = ""
for letter in sentence:
    word += letter
    if letter == " ":
        print(word[0])
        word = ""