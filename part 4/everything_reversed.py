# Write your solution here
def everything_reversed(customList : list) -> list:
    newList = []
    for i in customList:
        newList.append(i[::-1])
    return newList[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)