# Write your solution here
def most_common_character(customString : str) -> str:
    count = 0
    letter = ""
    for i in customString:
        if count < customString.count(i):
            count = customString.count(i)
            letter = i
    return letter

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))