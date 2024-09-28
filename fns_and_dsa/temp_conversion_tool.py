FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_ADDITION = 32

# Check if the global conversion factor CELSIUS_TO_FAHRENHEIT_FACTOR is defined correctly
def check_global_variables():
    if CELSIUS_TO_FAHRENHEIT_FACTOR != 9 / 5:
        raise ValueError("CELSIUS_TO_FAHRENHEIT_FACTOR is incorrectly defined.")
    if FAHRENHEIT_TO_CELSIUS_FACTOR != 5 / 9:
        raise ValueError("FAHRENHEIT_TO_CELSIUS_FACTOR is incorrectly defined.")

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_ADDITION) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_ADDITION

check_global_variables()
temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
if unit == "C":
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp}°F")
elif unit == "F":
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
