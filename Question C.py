"""
Write a Python program to convert temperatures to and from Celsius, Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in Celsius and f = temperature in Fahrenheit ]
Expected Output:
60°C is 140 in Fahrenheit
45°F is 7 in Celsius

"""
fahrenheit = 45
celsius = 60
in_celsius = (fahrenheit - 32) * 5/9
in_fahrenheit = (celsius * 9/5) + 32

print(' 60 degrees Celsius in Fahrenheit is:', in_fahrenheit)
print(' 45 degrees Fahrenheit in Celsius is:', in_celsius)



