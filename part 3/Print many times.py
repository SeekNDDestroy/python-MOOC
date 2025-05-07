# Write your solution here
def chessboard(times):
    for i in range(times):
        for j in range(times):
            if i % 2 == 0 or j % 2 == 0:
                print("1", end="")
            else:
                print("0", end="")
        print()


# Testing the function
if __name__ == "__main__":
    chessboard(3)
