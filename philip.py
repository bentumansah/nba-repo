temp_unit = input("Enter the unit of temperature, Celsius of Fahrenheit(C/F): ")
initial_temp = float(input("Enter the temperature: "))


if temp_unit == 'C':
    temp = ((initial_temp * 9 ) / 5 + 32)
    print(f"The temperature in Fahrenheit is {temp}°F")
elif temp_unit == 'F':
    temp = ((initial_temp - 32 ) * 5 / 9)
    print(f"The temperature in Celsius is {temp}°C")
else:
    print({temp_unit}," is an invalid unit for measuring temperature")