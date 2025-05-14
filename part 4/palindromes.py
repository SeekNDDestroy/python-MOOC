# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(customString : str) -> bool:
    string1 = customString
    string2 = customString[::-1]
    if string1 == string2:
        return True
    return False

while True:
    string = input("Please type in a palindrome:")
    if palindromes(string):
        print(f"{string} is a palindrome!")
        break;
    print(f"that wasn't a palindrome")