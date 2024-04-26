# PSEUDOCODE
# 1. Write a method in python to write multiple line of text Contents into a text file mylife.txt.

# MAIN CODE LINE

with open("mylife.py", "w") as text_file:
    while True:
        line_input = input("Enter a new line: ")
        text_file.write (line_input + "\n")

