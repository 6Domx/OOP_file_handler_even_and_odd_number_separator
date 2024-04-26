# PSEUDOCODE
# 1. Create a python program that will read a file containing 20 students' GWA
# 2. The Program should print the name of the Student who got the highest GWA with their GWA.

# MAIN CODE LINE

def print_highest_gwa(filename):
    highest_student = {"student_name": None, "gwa": 0.0}
    with open(filename, "r") as file:
        for line in file:
            student_name, gwa_str = line.strip().split()
            gwa = float(gwa_str)

            if gwa > highest_student["gwa"]:
                highest_student["student_name"] = student_name
                highest_student["gwa"] = gwa

    return highest_student

if __name__ == "__main__":
    filename = r"C:\Users\M2\Documents\CODING\python\OOP_file_handler_even_and_odd_number_separator\students_gwa.txt"

    highest_student = print_highest_gwa(filename)

    if highest_student["student_name"]:
        print(f"Student with the highest GWA: {highest_student['student_name']} ({highest_student['gwa']:.2f})")