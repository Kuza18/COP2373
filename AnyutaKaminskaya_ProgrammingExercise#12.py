# This program reads student exam grades from grades.csv, puts them in a
# numpy array, and prints stats for each exam, all exams combined,
# pass/fail counts, and the pass percentage.
import csv
import numpy as np

# Rounds every number to 2 decimal places.
# .tolist() turns the numpy array into a regular Python list, so
# it can print with commas.
def clean(values):
    return np.round(values, 2).tolist()

# Reads grades.csv and returns the exam scores as a 2-D numpy array.
def load_grades_csv():
    # Open file, read it and create a list of lists.
    with open("grades.csv", "r") as file:
        rows = list(csv.reader(file))

    # Build a new list that holds ONLY the exam scores.
    grades = []
    # rows[1:] skips the header row and the columns 2, 3, 4 contain the exams.
    for row in rows[1:]:
        grades.append([int(row[2]), int(row[3]), int(row[4])])

    #   - each ROW is one student
    #   - each COLUMN is one exam
    return np.array(grades)


# Prints the mean, median, standard deviation, min, and max for
# EACH exam.
def print_exam_stats(grades):
    # axis=0 gives one answer per column (per exam).
    print("\nStats for each exam:")
    print("Mean:", clean(np.mean(grades, axis=0))) # Average score
    print("Median:", clean(np.median(grades, axis=0))) # Middle score
    print("Std dev:", clean(np.std(grades, axis=0))) # How spread out scores are from mean
    print("Min:", clean(np.min(grades, axis=0))) # Lowest score
    print("Max:", clean(np.max(grades, axis=0))) # Highest score


# Prints the same 5 stats, but for ALL the grades together.
def print_overall_stats(grades):
    # No axis = use every grade in the whole array
    print("\nOverall Stats:")
    print("Mean:", clean(np.mean(grades)))
    print("Median:", clean(np.median(grades)))
    print("Std dev:", clean(np.std(grades)))
    print("Min:", clean(np.min(grades)))
    print("Max:", clean(np.max(grades)))


# Counts how many students passed and failed each exam.
# A passing grade is 60 or above.
def print_pass_fail(grades):
    # grades >= 60 makes an array of True/False.
    # When you sum it, True counts as 1, so the sum = number of passes.
    print("\n# of students who passed each exam:", np.sum(grades >= 60, axis=0))
    print("# that failed each exam:", np.sum(grades < 60, axis=0))

    # Passing / total grades * 100 = passing%
    percent = np.sum(grades >= 60) / np.size(grades) * 100
    print("Overall passing percentage:", round(percent, 2), "%")

 # Runs the whole program in order.
def main():
    # Step 1: load the CSV into a numpy array.
    grades = load_grades_csv()

    # Step 2: print the first 5 rows to see the data's structure.
    print("~~~ Exam Scores Formating:\n~~~ [Exam 1, Exam 2, Exam 3]\n~~~ example scores for first 5 students --> ")
    print(grades[:5])

    # Steps 3: print the statistics.
    print_exam_stats(grades)
    print_overall_stats(grades)
    print_pass_fail(grades)

# Run the program.
main()









