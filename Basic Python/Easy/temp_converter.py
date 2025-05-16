"""
Temperature Converter
Convert temperature from Celsius to Fahrenheit.
"""

temp_c = int(input("Enter temprature in Celsius (°C): "))
temp_f = (temp_c * (9/5)) + 32
print(f"The temprature in Fahrenheit (°F): {temp_f:.2f}")