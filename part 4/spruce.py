# Write your solution here
# You can test your function by calling it within the following block
def spruce(height):
    print("a spruce!")
    patternMultiplier = 1
    for i in range(height, 0, -1):
        print(" " * (i - 1) + "*" * patternMultiplier)
        patternMultiplier += 2
    print(" " * ((patternMultiplier // 2) - 1) + "*")

        

if __name__ == "__main__":
    spruce(5)