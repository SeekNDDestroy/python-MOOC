# Write your solution here
def length_of_longest(customList : list) -> int:
    best = ""
    for i in customList:
        if len(i) > len(best):
            best = i
    return len(best)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)