number = int(input("Please type in a number"))
i = 1
current = 0
next = 0
while i <= number:
    current = i
    i += 1
    next = i
    if next > number:
        print(current)
        break
    print(next)
    if next > number:
        break
    print(current)
    i+= 1
    