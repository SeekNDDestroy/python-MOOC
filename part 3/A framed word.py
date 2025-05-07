string = input("Word:")
print("*" * 30)
if len(string) % 2 == 0:
    print("*" + " " * int((28 - len(string)) / 2) + string + " " * int((28 - len(string)) / 2) +"*")
else:
    string = ("*" + " " * ((28 - len(string))//2 + 1)+ string + " " * ((28 - len(string))//2 ) + "*")
    print(string)
print("*" * 30)



