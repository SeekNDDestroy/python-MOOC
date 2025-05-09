# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block

def triangle(size, character):
    # You should call function line here with proper parameters
    for i in range(size):
        line(i, character)

def line(size, character):
    print(character * (size + 1))

def rectangle(width, size, character):
    for i in range(size):
        print(character * width)

def shape(triSize, triShape, squareSize, squareShape):
    triangle(triSize, triShape)
    rectangle(triSize, squareSize, squareShape)




if __name__ == "__main__":
    shape(5, "X", 3, "*")