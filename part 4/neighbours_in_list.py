# Write your solution here
def longest_series_of_neighbours(customList : list) -> int:
    oldCount = 0
    count = 0
    for i in range(len(customList) - 1):
        value = customList[i]
        if customList[i + 1] == customList[i] + 1 or customList[i + 1] == customList[i] - 1:
            count += 1
        elif oldCount < count:
            oldCount = count
            count = 0
        else:
            count = 0
    if oldCount > count:
        print(f"count {oldCount + 1}")
        return oldCount + 1;
    print(f"old count {count + 1}")     
    return count + 1;    


if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25, 30]
    print(longest_series_of_neighbours(my_list))