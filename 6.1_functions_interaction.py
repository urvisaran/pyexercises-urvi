"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. Input: A list of drink names.
# 2. Process: One function counts drinks, one calculates total name length,
#    and one calculates average name length.
# 3. Output: The number of drinks longer than the average.
# 4. The fourth function answers how many drink names are above average.
#    Splitting makes each calculation easier to test separately.


# Your code below
drinks = ["vodka", "wine", "tequila", "beer", "gin", "whiskey", "rum", "rosé"]

def count_drinks(drinks):
    return len(drinks)

def longest_drink_name(drinks):
    longest = 0
    for drink in drinks:
        if len(drink) > longest:
            longest = len(drink)
    return longest

def shortest_drink_name(drinks):
    shortest = 100
    for drink in drinks:
        if len(drink) < shortest:
            shortest = len(drink)
    return shortest

def compare_drink_names(drinks):
    total = count_drinks(drinks)
    longest = longest_drink_name(drinks)
    shortest = shortest_drink_name(drinks)

    if total > longest:
        return "There are more drinks than the length of the longest name."
    else:
        return "The longest drink name is longer than the number of drinks."

print("Number of drinks:", count_drinks(drinks))
print("Longest name length:", longest_drink_name(drinks))
print("Shortest name length:", shortest_drink_name(drinks))
print("Comparison:", compare_drink_names(drinks))