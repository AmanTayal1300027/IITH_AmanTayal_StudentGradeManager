"""
Student Grade Manager (CLI)
----------------------------
This script allows users to:
- View all student grades in tabular format
- Add, remove, or update student records
- Display bar charts of student performance
- Calculate and append average and highest class grades
Data is stored in a local CSV file.
"""

import csv
import os
from tabulate import tabulate

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # one level up from /src
ASSETS_DIR = os.path.join(ROOT_DIR, "assets", "other-assets")
FILENAME = os.path.join(ASSETS_DIR, "students.csv")

HEADERS = ["ID", "Name", "Grade"]

# Ensure assets/other-assets exists
os.makedirs(ASSETS_DIR, exist_ok=True)

#returns true if file exists
file_exists = os.path.exists(FILENAME)

#if file does not exist then, it appends the header to the top of file. If it exists then this script is skipped
if not file_exists:
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Grade"])

#checks whether a number is a floating point number
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
#reads the csv file data, and writes it to command line
def show_student_data():
    print("\nSTUDENT GRADES:")
    print('-'*60)
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        data = list(reader)
    print(tabulate(data, headers="firstrow", tablefmt="grid"))
    print('-'*60)

#allows user to view only a particular students Grades by inputing his name
def show_particular_student_data():
    student_id = input("Enter Student ID: ")
    exist = 0
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        data = list(reader)

        headers = data[0]

        for row in data[1:]:
            if row[0] == str(student_id):
                print(tabulate([row], headers=headers, tablefmt="grid"))
                exist = 1
                break
        if exist==0:
            print('-'*60)
            print(f"Student with ID {student_id} not found")
            print('-'*60)

#used to insert new student in the csv file
def add_new_student():
    ID = input("Enter ID: ")
    NAME = input("Enter Name: ")
    GRADE = input("Enter Grade: ")

    if not isfloat(GRADE):
        print('-'*60)
        print("Invalid input. Grade should be a floating point number")
        print('-'*60)
        return

    new_student = [ID, NAME, GRADE]

    with open(FILENAME, mode="r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)

        rows = [header]

        for row in reader:
            if row[0] == ID:
                print('-'*60)
                print(f"Student with ID = {ID} already exists")
                print('-'*60)
                return
                    
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(new_student)
    print('-'*60)
    print(f"Student {new_student[1]} added successfully.")
    print('-'*60)

#used to remove a particular students data
def remove_student():
    student_id = input("Enter Student ID: ")
    found = False
    updated_data = []

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        data = list(reader)
        headers = data[0]
        
        for row in data[1:]:
            if row[0] == str(student_id):
                found = True
            else:
                updated_data.append(row)

    if found:
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(updated_data)
        print('-'*60)
        print(f"Student with ID {student_id} removed successfully.")
        print('-'*60)
    else:
        print('-'*60)
        print(f"Student with ID {student_id} not found.")
        print('-'*60)

#upadates student's data by first input of student ID and then input his new grade
def update_student_data():
    student_id = input("Enter Student ID to update: ")
    new_grade = input("Enter new grade: ")
    if not isfloat(new_grade):
        print('-'*60)
        print("Invalid input. Grades are floating point integers")
        print('-'*60)
        return

    found = False
    updated_data = []

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        data = list(reader)
        headers = data[0]
        updated_data.append(headers)
        
        for row in data[1:]:
            if row[0] == str(student_id):
                found = True
                if new_grade:
                    row[2] = str(new_grade)
            updated_data.append(row)

    if found:
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_data)
        print('-'*60)
        print(f"Student with ID {student_id} updated successfully.")
        print('-'*60)
    else:
        print('-'*60)
        print(f"Student with ID {student_id} not found.")
        print('-'*60)

#displays a bar chart of the class
def display_barchart():

    av_col = "Average Grade"
    hm_col = "Highest Grade"

    students = []
    grades = []

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
    
        for row in reader:
            if isfloat(row[2]) and row[0]!=av_col and row[0]!=hm_col:
                students.append(row[1])
                grades.append(float(row[2]))
            if row[0] == hm_col:
                max = float(row[2])

    scaled_grades = [int((g / max) * 50) for g in grades] #Normalize grades for chart scale (max 50 bars)

    print("\nSTUDENT GRADES")
    print("-" * 60)

    for i in range(len(students)):
        print(f"{students[i]:<15}: {'|' * scaled_grades[i]} {grades[i]}")
        print(" " * 100)

    print("-" * 60)    

#calculates average marks and highest marks
def calculate_highest_average_grade():
    av_col = "Average Grade"
    hm_col = "Highest Grade"

    with open(FILENAME, mode="r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)

        rows = [header]
        for row in reader:
            if row[0] != av_col and row[0] != hm_col:
                rows.append(row)

    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


    grades = []
    max=float('-inf')
    
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        data = list(reader)

        for row in data[1:]:
            if isfloat(row[2]) and row[0]!=av_col and row[0]!=hm_col:
                grades.append(float(row[2]))
    
    for st_grades in grades:
        if st_grades>max:
            max = st_grades

    if grades:
        avg_grade = sum(grades) / len(grades)
    else:
        avg_grade = 0

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Average Grade", "",f"{avg_grade:.2f}"])
        writer.writerow(["Highest Grade", "",f"{max:.2f}"])

    print('-'*60)
    print(f"\nAverage grade {avg_grade:.2f} added at the end of the file.")
    print(f"Highest grade {max:.2f} added at the end of the file.\n")
    print('-'*60)
    # Remove previous summary rows (Average Grade, Highest Grade) before re-calculating


option = 'y'

while not option == 'q':
    print(' '*60)
    print('#'*60)
    print("#  Welcome to Student Grade Manager                        #")
    print("#  Enter any one of the options to continue:               #")
    print("#  1. To display all Students grades                       #")
    print("#  2. Display a particular Students grades                 #")
    print("#  3. Add new student                                      #")
    print("#  4. Remove student                                       #")
    print("#  5. Update student's grades                              #")
    print("#  6. Display bar chart                                    #")
    print("#  7. Display the highest grade and average class grade    #")
    print("#  q. Quit                                                 #")
    print('#'*60)

    option = input("Enter option: ")

    if option=='1':
        show_student_data()

    if option=='2':
        show_particular_student_data()

    if option=='3':
        add_new_student()

    if option=='4':
        remove_student()

    if option=='5':
        update_student_data()
    
    if option=='6':
        display_barchart()
    
    if option == '7':
        calculate_highest_average_grade()
