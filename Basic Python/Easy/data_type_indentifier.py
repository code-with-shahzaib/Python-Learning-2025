"""
Data Type Identifier
Take input from the user and print the type of the input.
"""

int_data = int(input("Enter numberic data to know it's type in python: "))
float_data = float(input("Enter decimal  data to know it's type in python: "))
str_data = input("Enter sentece to know it's type in python: ")

print(f"The type of numberic data is {type(int_data)}")
print(f"The type of decimal data is {type(float_data)}")
print(f"The type of sentence is {type(str_data)}")