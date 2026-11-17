"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My function name, and why return rather than print:


# Your code below
drinks = ["vodka", "wine", "tequila", "beer", "gin", "whiskey", "rum", "rosé"]

def count_drinks_with_letter(drinks, letter):
    count = 0
    for drink in drinks:
        if letter in drink:
            count += 1
    return count

# Return allows us to reuse the result, whereas print only displays it.

print("Number of drinks containing 'e':", count_drinks_with_letter(drinks, "e"))
print("Number of drinks containing 'w':", count_drinks_with_letter(drinks, "w"))
print("Number of drinks containing 'o':", count_drinks_with_letter(drinks, "o"))

# An empty list returns 0, which is acceptable because it contains no drinks.
print("Number of drinks in an empty list:", count_drinks_with_letter([], "e"))