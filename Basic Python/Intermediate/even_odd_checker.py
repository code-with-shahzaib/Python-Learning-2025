"""
Check Even or Odd
Ask the user for a number and print whether it's even or odd.
"""

number = int(input("Enter a number: "))

if (number % 2 == 0):
    print(f"Number {number} is Even.")

else:
    print(f"Number {number} is Odd.")