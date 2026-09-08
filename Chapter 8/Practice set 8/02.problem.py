'''
c/5= (f-32 )/9
'''
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
n = int(input("Enter temperature in Celsius: "))
f = celsius_to_fahrenheit(n)
x = round(f, 2)
print("Temperature in Fahrenheit:", x)