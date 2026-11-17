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

# 1. In:
# 2. Process:
# 3. Out, file name and columns:
# 4. Why these columns, and what this file is for:


# Your code below
# 1. In: Drink name, category, price and date entered by the user.
# 2. Process: Collect the details, check that the price is valid,
#    and add the entry to the CSV file.
# 3. Out: drinks_log.csv with columns Drink, Category, Price and Date.
# 4. I chose these columns to keep track of drinks, their costs and purchase dates.
#    After 200 rows, I could analyse spending and see which drinks I buy most often.

import pandas as pd
import os

df = "drinks_log.csv"

drink = input("Enter drink name: ")
category = input("Enter drink category: ")
price = input("Enter price: ")
date = input("Enter date (DD/MM/YYYY): ")

# Check that price is a valid number
while True:
    try:
        price = float(price)
        if price < 0:
            raise ValueError
        break
    except ValueError:
        price = input("Enter a valid positive price: ")

# Create a new entry
new_entry = pd.DataFrame({
    "Drink": [drink],
    "Category": [category],
    "Price": [price],
    "Date": [date]
})

# Add entry without overwriting previous entries
new_entry.to_csv(df, mode="a", header=not os.path.exists(df), index=False)

print("Entry saved successfully!")
