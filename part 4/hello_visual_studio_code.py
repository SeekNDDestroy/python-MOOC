# Write your solution here
while True:
    editor = input("Editor:")
    editor = editor.lower()
    if editor == "word":
        print("awful")
    elif editor == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")