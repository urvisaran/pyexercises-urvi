"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""


# 1. In:
# A number entered by the user.

# 2. Process:
# Ask the user for a number and divide 100 by it.
# Repeat the process for a maximum of 3 attempts.
# Handle invalid input and division by zero separately.

# 3. Out:
# The result of the division or an error message.

# 4. The two failures, and whether they deserve the same message:
# Zero causes a ZeroDivisionError because division by zero is not possible.
# Entering text such as "abc" causes a ValueError because it is not a number.
# They should have different messages to explain what went wrong.

# Catching errors separately makes it easier to give the user
# the correct explanation for each problem.


attempts = 0

while attempts < 3:
    try:
        number = float(input("Enter a number: "))
        result = 100 / number
        print("Result:", result)
        break

    except ValueError:
        print("Please enter a valid number.")

    except ZeroDivisionError:
        print("You cannot divide by zero.")

    attempts = attempts + 1

if attempts == 3:
    print("You have used all 3 attempts.")
