# PSEUDOCODE
# 1. Create a python program that will read a file containing 20 students' GWA
# 2. The Program should print the name of the Student who got the highest GWA with their GWA.

# MAIN CODE LINE

def print_highest_gwa(students_gwa):

    highest_student = {"student_name": None, "gwa": 0.0}
    with open("C:\Users\M2\Documents\CODING\python\OOP_file_handler_even_and_odd_number_separator\students_gwa.txt", "r") as file:
        for line in file:
            student_name, gwa = line.strip().split()
            gwa = float(gwa)

            if gwa > highest_student["gwa"]:
                highest_student["student_name"] = student_name
                highest_student["gwa"] = gwa

    return print_highest_gwa