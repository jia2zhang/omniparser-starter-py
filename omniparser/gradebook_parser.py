


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
import json

# Parsing CSV file - PANDAS WAY
def calculate_average_grade_from_csv(my_csv_filepath):
    gradebook = pandas.read_csv(my_csv_filepath)
    
    # # Method 1 using statistics module
    # rows = gradebook.to_dict("records")
    # grades = [r["final_grade"] for r in rows]
    # avg_grade = statistics.mean(grades)
    
    # # Method 2 using statistics module
    # grades = gradebook["final_grade"].to_list()
    # avg_grade = statistics.mean(grades)
    
    # # Method 3
    avg_grade = gradebook["final_grade"].mean()

    return avg_grade

if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK CSV FILES HERE...")
    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
    # print(gradebook_filepath)
    # breakpoint()
    avg = calculate_average_grade_from_csv(gradebook_filepath)
    print(avg)

# CHECK-IN: avg for 2018 is 83.64, 2019 is 90.64

# URL = os.path.join(os.path.dirname(__file__),"..","data","gradebook_2019.json")
# gradebook_json = pandas.read_json(URL, orient='records')
# print(gradebook_json.students["finalgrade"])
# def calculate_average_grade_from_json(x):
#     #breakpoint()

#     with open(x, "r") as f:
#         print(type(f))
#         file_contents = f.read()
#         print(type(file_contents)) #> str

#     gradebook = json.loads(file_contents)

#     print(type(gradebook))
#     print(gradebook)


#     return 10000
# Parsing JSON file  - PANDAS WAY
def calculate_average_grade_from_json(x):
    with open(x,"r") as f:
        file_contents = f.read()

    gradebook = json.loads(file_contents)
    #print(type(gradebook))
    #print(gradebook)
    


    # grades = [r["finalgrade"] for r in rows]
    # print(grades)
    # avg_grade = statistics.mean(grades)
    # print(avg_grade)

if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK JSON FILES HERE...")
    gradebook_filepath = os.path.join(os.path.dirname(__file__),"..","data","gradebook_2018.json")
    print(gradebook_filepath)
    print(os.path.isfile(gradebook_filepath))
    avg = calculate_average_grade_from_json(gradebook_filepath)
    print(avg)
