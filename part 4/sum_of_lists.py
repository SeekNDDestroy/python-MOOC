# Write your solution here
def list_sum(listA : list, listB : list) -> list:
    newList = []
    for i in range(len(listA)):
        newList.append(listA[i] + listB[i])
    return newList

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]