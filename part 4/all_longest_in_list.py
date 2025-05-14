# Write your solution here
def all_the_longest(customList : list) -> list:
    newList = []
    longest = " "
    for i in customList:
        if len(i) > len(longest):
            longest = i
    for i in customList:
        if len(i) == len(longest):
            newList.append(i)
    return newList

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']