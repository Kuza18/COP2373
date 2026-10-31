# This module lets you write and read CSV files
import csv

# Asks instructor for student info and writes into grades.csv
def create_grades_file():
    # Ask how many students will be entered
    num_students = int(input("How many students do you want to enter? "))

    # 'with' opens the file and closes it automatically when done.
    # 'w' means write mode.
    # newline="" prevents blank lines between rows.
    with open("grades.csv", "w", newline="") as file:
       writer = csv.writer(file)

       # Write the header row first
       writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

       # Repeat once for each student
       for i in range(num_students):
           print("\nStudent", i + 1)

           # Names are strings
           first_name = input("First Name: ")
           last_name = input("Last Name: ")

           # Grades are integers
           exam1 = int(input("Exam 1 grade: "))
           exam2 = int(input("Exam 2 grade: "))
           exam3 = int(input("Exam 3 grade: "))

           # Writes this student as 1 row (record) in the file.
           writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\ngrades.csv has been created")

# Reads grades.csv and displays the data in a table.
def display_grades():
     # 'r' means read mode
     with open("grades.csv", "r") as file:
         reader = csv.reader(file)

         # Each row comes back as a list, like ["Bob", "White", "90", "80", "70"]
         for row in reader:
             # <15 left-aligns in 15 spaces, >8 right-aligns in 8 spaces.
             print(f"{row[0]:<15}{row[1]:<15}{row[2]:>8}{row[3]:>8}{row[4]:>8}")

# Runs both programs in order
def main():
    create_grades_file()
    display_grades()

main()