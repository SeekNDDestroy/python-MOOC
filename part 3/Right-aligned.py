string = input("Please type in a string:")
stringLength = len(string)

toBeFilled = 20 - stringLength
print("*" * toBeFilled + string)