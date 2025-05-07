string1 = input("Please type in string 1:")
string2 = input("Please type in string 2:")

string1Len = len(string1)
string2Len = len(string2)

if string1Len == string2Len:
    print("The strings are equally long")
elif string1Len > string2Len:
    print(f"{string1} is longer")
else:
    print(f"{string2} is longer")