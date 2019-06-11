
print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

# omniparser/gradebook_parser.py
# student_id,final_grade
# 1,76.7
# 2,85.1
# 3,50.3
# 4,89.8
# 5,97.4
# 6,75.5
# 7,87.2
# 8,88.0
# 9,93.9
# 10,92.5

## Import the necessary packages for the program
import pandas
import os
import statistics

# Parsing CSV file - TRADITIONAL WAY


# Parsing JSON file  - TRADITIONAL WAY


# Parsing CSV file - PANDAS WAY
def calculate_avg_grade_csv(my_csv_filepath):
    gradebook = pandas.read_csv(my_csv_filepath)
    rows = gradebook.to_dict("records")
    grades = [r["final_grade"] for r in rows]
    avg_grade = statistics.mean(grades)
    return avg_grade


print(gradebook)


# Parsing JSON file  - PANDAS WAY


