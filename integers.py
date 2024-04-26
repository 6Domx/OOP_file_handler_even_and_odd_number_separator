# PSEUDOCODE 
# 1. Write a python program that will create two separate text files after reading the source file named integers.
# 2. First file should contain the square of all integers.
# 3. Second file should contain the cube of all integers.

# MAIN CODE LINE

def integer_cb_sqr(main_file):

    with open(main_file, "r") as text_file:
        integers = [int(line.strip()) for line in text_file.readlines()]

    with open("double.txt", "w") as sqr_file, open("triple.txt", "w") as cb_file:
        for num in integers:
            if num % 2 == 0:
                sqr_file.write(str(num ** 2) + "\n")

            else:
                cb_file.write(str(num ** 3) + "\n")

integer_cb_sqr('integers_values.txt') 