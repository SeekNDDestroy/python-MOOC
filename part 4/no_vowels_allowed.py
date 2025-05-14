# Write your solution here
def no_vowels(customString : str) -> str:
    string = ""
    for i in customString:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            string += i
    return string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))