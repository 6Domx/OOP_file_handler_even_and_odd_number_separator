# PSEUDOCODE
# 1. Write a method in python to write multiple line of text Contents into a text file mylife.txt.

# MAIN CODE LINE

def multiple_line_writing(filename, lines):
    with open(filename, "w") as f:
        f.writelines(lines)

