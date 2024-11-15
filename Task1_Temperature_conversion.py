def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def convert_temperature():
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()

    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        print(f"\n{temperature}°C is equivalent to:")
        print(f"{fahrenheit:.2f}°F")
        print(f"{kelvin:.2f}K")

    elif unit == 'F':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        print(f"\n{temperature}°F is equivalent to:")
        print(f"{celsius:.2f}°C")
        print(f"{kelvin:.2f}K")

    elif unit == 'K':
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        print(f"\n{temperature}K is equivalent to:")
        print(f"{celsius:.2f}°C")
        print(f"{fahrenheit:.2f}°F")

    else:
        print("Invalid unit entered. Please use 'C', 'F', or 'K'.")

# Run the temperature conversion program
convert_temperature()
