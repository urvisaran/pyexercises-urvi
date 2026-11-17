"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Some names have inconsistent capitalisation.
# - Some lines have leading spaces.
# - There are blank lines between some names.
# - Some names have first and last names with different capitalisation.

# 1. In:
# A text file containing people's first and last names, one person per line.

# 2. Process, problem by problem:
# - Convert names to consistent capitalisation using title case.
# - Remove leading and trailing spaces from each line.
# - Remove blank lines.
# - Split each name into first name and last name so it can be sorted by last name.

# 3. Out:
# A new text file containing cleaned names, sorted alphabetically by last name.

# 4. How I decide which word is the last name:
# The second word on each line is treated as the last name.

# Your code below
names = []

with open("names.txt", "r") as file:
    for line in file:
        name = line.strip()

        if name != "":
            name = name.title()
            names.append(name)

names.sort(key=lambda name: name.split()[1])

with open("cleaned_names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
