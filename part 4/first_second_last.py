# Write your solution here
# You can test your function by calling it within the following block
def first_word(sentence):
    word = ""
    for i in sentence:
        if i == " ":
            return word
        word += i

def second_word(senence):
    word = ""
    flag = 0
    for i in sentence:
        if i == " ":
            flag += 1
            if flag == 2:
                return word
            word = ""
            continue
        word += i
    
def last_word(sentence):
    word = ""
    for i in range((len(sentence) - 1), 0, -1):
        if sentence[i] == " ":
            word1 = word[::-1]
            return word1
        word += sentence[i]
    



if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))