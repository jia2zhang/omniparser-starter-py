


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

# Parsing CSV file - PANDAS WAY
def calculate_average_grade_from_csv(my_csv_filepath):
    gradebook = pandas.read_csv(my_csv_filepath)
    rows = gradebook.to_dict("records")
    grades = [r["final_grade"] for r in rows]
    print(grades)
    avg_grade = statistics.mean(grades)
    return avg_grade

if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")
    gradebook_filepath = os.path.join(os.path.dirname(__file__),"..","data","gradebook_2019.csv")
    avg = calculate_average_grade_from_csv(gradebook_filepath)
    print(avg)

# CHECK-IN: avg for 2018 is 83.64, 2019 is 90.64

## TODO: debug the json parsing portion below:
URL = os.path.join(os.path.dirname(__file__),"..","data","gradebook_2019.json")
gradebook_json = pandas.read_json(URL, orient='records')
print(gradebook_json.students["finalgrade"])

# Parsing JSON file  - PANDAS WAY
def calculate_average_grade_from_json(my_json_filepath):
    gradebook = pandas.read_json(my_json_filepath)
    print(type(gradebook))
    rows = gradebook.read_json(_, orient='records')
    print(type(rows["finalgrade"]))
    # grades = [r["finalgrade"] for r in rows]
    # print(grades)
    # avg_grade = statistics.mean(grades)
    # print(avg_grade)

if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")
    gradebook_filepath = os.path.join(os.path.dirname(__file__),"..","data","gradebook_2019.json")
    # avg = calculate_average_grade_from_json(gradebook_filepath)
    # print(avg)
