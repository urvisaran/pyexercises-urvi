"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""


# 1. In: First name, last name, email and student number.
# 2. Process: Ask the user for each detail and check that none are empty.
# 3. Out: 7.0_student_data.csv with four columns:
#    first_name, last_name, email, student_number.
# 4. I chose these columns to maintain a student record.
#    With 200 rows, I could organise students or analyse the data.

import pandas as pd
import os

filename = "7.0_student_data.csv"

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
email = input("Enter email: ").strip()
student_number = input("Enter student number: ").strip()

while not first_name or not last_name or not email or not student_number:
    print("All fields are required.")
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    email = input("Enter email: ").strip()
    student_number = input("Enter student number: ").strip()

new_student = pd.DataFrame({
    "first_name": [first_name],
    "last_name": [last_name],
    "email": [email],
    "student_number": [student_number]
})

new_student.to_csv(filename, mode="a", header=not os.path.exists(filename) or os.path.getsize(filename) == 0, index=False)

print("Student record saved!")

