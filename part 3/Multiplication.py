number = int(input("Please type in a number"))

i = 1; j = 1

while i <= number:
    while j <= number:
        print(f"{i} x {j} = {i * j}")
        j += 1
    i += 1
    j = 1