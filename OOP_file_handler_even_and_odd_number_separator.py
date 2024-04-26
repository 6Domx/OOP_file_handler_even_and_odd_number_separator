# PSEUDOCODE
# 1. Create a Program that reads a text file.
# 2. It should contain 20 integers.
# 3. The Program should be able to create two more new text file.
# 4. The first text file should be named even.txt and it should contain all the even numbers
# 5. The second text file should be named odd.txt and it should contain all the odd numbers.

# MAIN CODE LINE

def evn_odd_separate(numbers):

    with open ("numbers.txt", "r") as main_file:
        numbers = [int(line.strip()) for line in main_file]

    evn_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    
