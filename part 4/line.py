# Write your solution here
def line(times, string):
    if not string:
        string = "*"
    print(string[0] * times)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")