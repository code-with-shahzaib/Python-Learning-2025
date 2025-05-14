"""
Swap Two Variables
Swap two numbers using a third variable.
"""

a = int(input("Enter a number for a: "))
b = input("Enter a word for b: ")

print(f"Original Values a = {a}, b = {b}")
a, b = b, a
print(f"Swapped Values a = {a}, b = {b}")