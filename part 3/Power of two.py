upperLimit = int(input("Upper limit:"))
number = 0
power = 0
while (2 ** number) <= upperLimit:
    power = 2 ** number
    print(power)
    number += 1