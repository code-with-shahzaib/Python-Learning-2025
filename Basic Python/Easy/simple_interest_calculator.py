"""
Simple Interest Calculator
Calculate simple interest using the formula: SI = (P x R x T) / 100.
P = Principal amount (the initial sum of money)
R = Rate of interest (in percentage)
T = Time (in years)
"""

principal_amount = float(input("Enter your principal amount: "))
interest_rate = float(input("Enter interest in percentage: "))
time = int(input("Enter time in years: "))

simple_interest = (principal_amount * interest_rate * time) / 100

print(f"The interest amount after calculation is: {simple_interest}")