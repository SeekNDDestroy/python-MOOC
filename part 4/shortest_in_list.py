# Write your solution here
def shortest(customList : list) -> str:
    word = customList[0]
    for i in customList:
        if len(word) > len(i):
            word = i
    return word

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)