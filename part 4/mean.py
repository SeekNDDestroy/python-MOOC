# Write your solution here
def mean(customList : list) -> int:
    sumOfElements = sum(customList)
    length = len(customList)
    return sumOfElements / length
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)