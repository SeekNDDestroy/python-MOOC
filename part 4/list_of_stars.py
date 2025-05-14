# Write your solution here
def list_of_stars(customList : list):
    for i in customList:
        print("*" * i)

if __name__ == "__main__":
    list_of_stars([1, 2, 3, 4,1, 3])