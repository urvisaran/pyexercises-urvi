"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# Two strings: "apple" and "Apple".

# 2. What happens to it?
# Python compares the two strings using comparison operators.
# It also checks the logical combinations of those comparisons.

# 3. Out:
# A readable table showing the result of each comparison
# and logical combination.

# 4. Which two values did I pick, and which comparison result surprised me?
# I picked "apple" and "Apple".
# I was surprised that "apple" is greater than "Apple"
# because Python considers capital letters different from lowercase letters.

a = "apple"
b = "Apple"

print("Comparison          Result")
print("---------------------------")

print("a == b              ", a == b)
print("a != b              ", a != b)
print("a > b               ", a > b)
print("a < b               ", a < b)
print("a >= b              ", a >= b)
print("a <= b              ", a <= b)

print("\nLogical combinations")
print("---------------------------")

print("(a == b) and (a != b)", (a == b) and (a != b))
print("(a == b) or (a != b) ", (a == b) or (a != b))
print("not (a == b)        ", not (a == b))
