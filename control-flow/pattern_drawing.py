# pattern_drawing.py
# This script prints a square pattern of asterisks (*) based on user input using nested loops.

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for each row
while row < size:
    # Inner for loop to print '*' 'size' times on the same line
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after completing a row
    row += 1