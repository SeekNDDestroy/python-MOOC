string = input("Please type in a string:")
lengthOfString = len(string)
if string[1] == string[-2]:
    print("The second and the second to last characters are", string[1])
else:
    print("The second and the second to last characters are different")