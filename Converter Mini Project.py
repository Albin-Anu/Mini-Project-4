# Unit Converter Mini Project
# Author: Albin Anu

def length_converter():
    print("\n--- Length Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Meters to Feet")
    print("4. Feet to Meters")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        km = float(input("Enter value in kilometers: "))
        print(f"{km} km = {km * 0.621371:.2f} miles")

    elif choice == '2':
        miles = float(input("Enter value in miles: "))
        print(f"{miles} miles = {miles / 0.621371:.2f} km")

    elif choice == '3':
        meters = float(input("Enter value in meters: "))
        print(f"{meters} meters = {meters * 3.28084:.2f} feet")

    elif choice == '4':
        feet = float(input("Enter value in feet: "))
        print(f"{feet} feet = {feet / 3.28084:.2f} meters")

    else:
        print("Invalid choice!")


def weight_converter():
    print("\n--- Weight Converter ---")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Grams to Kilograms")
    print("4. Kilograms to Grams")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        kg = float(input("Enter value in kilograms: "))
        print(f"{kg} kg = {kg * 2.20462:.2f} pounds")

    elif choice == '2':
        lb = float(input("Enter value in pounds: "))
        print(f"{lb} pounds = {lb / 2.20462:.2f} kg")

    elif choice == '3':
        g = float(input("Enter value in grams: "))
        print(f"{g} grams = {g / 1000:.2f} kg")

    elif choice == '4':
        kg = float(input("Enter value in kilograms: "))
        print(f"{kg} kg = {kg * 1000:.2f} grams")

    else:
        print("Invalid choice!")


def temperature_converter():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {(c * 9/5) + 32:.2f}°F")

    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {(f - 32) * 5/9:.2f}°C")

    elif choice == '3':
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {c + 273.15:.2f} K")

    elif choice == '4':
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k} K = {k - 273.15:.2f}°C")

    else:
        print("Invalid choice!")


def main():
    while True:
        print("\n===== Unit Converter =====")
        print("1. Length Converter")
        print("2. Weight Converter")
        print("3. Temperature Converter")
        print("4. Exit")

        option = input("Choose a category (1-4): ")

        if option == '1':
            length_converter()
        elif option == '2':
            weight_converter()
        elif option == '3':
            temperature_converter()
        elif option == '4':
            print("Thank you for using Unit Converter! 😊")
            break
        else:
            print("Invalid input! Please enter 1-4.")


if __name__ == "__main__":
    main()
