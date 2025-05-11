# Write your solution here
numbers = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index:"))
    if index == -1: break
    new_value = int(input("New value:"))
    numbers[index] = new_value
    print(numbers)
