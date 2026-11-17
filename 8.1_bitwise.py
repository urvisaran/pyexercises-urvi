"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""


# 1. In:
# Two sets of campaign permissions represented as numbers.

# 2. What happens to it?
# Combine permissions using OR.
# Check if a permission exists using AND.
# Add a permission using OR.
# Remove a permission using AND and NOT.

# 3. Out:
# The permissions at each step, displayed in binary.

# 4. What are my permissions about?
# They are permissions for a fashion marketing campaign.
# 1 = View, 2 = Edit, 4 = Publish.


view = 1
edit = 2
publish = 4

# Combine two permissions
permissions = view | edit
print("Combined permissions:", bin(permissions))

# Check if publish permission is present
print("Can publish:", bool(permissions & publish))

# Add publish permission
permissions = permissions | publish
print("After adding publish:", bin(permissions))

# Remove edit permission
permissions = permissions & ~edit
print("After removing edit:", bin(permissions))
