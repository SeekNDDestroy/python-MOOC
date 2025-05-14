# Write your solution here
def even_numbers(customList : list) -> list:
    newList = []
    for i in customList:
        if i % 2 == 0:
            newList.append(i)
    return newList

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)