number = int(input("Please type in a number"))
i = number - 1
num = 1
if number % 2 != 0:
    while i >= 0:
        print(num)
        if i == 0:
            break
        print(num + i)
        num += 1
        i -= 2
else:
    while i > 0:
        print(num)
        print(num + i)
        num += 1
        i -= 2