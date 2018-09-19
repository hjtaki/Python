# Exercise 2
name = input("Enter your name: ")
print("Hello " + name)


# Exercise 3
hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

print("Pay:", hours * rate)


# Exercise 4
# print the result value and the type
width = 17
height = 12.0
# 1
print(width // 2, type(width // 2))
# 2
print(width / 2.0, type(width / 2.0))
# 3
print(height / 3, type(height / 3))
# 4
print(1 + 2 * 5, type(1 + 2 * 5))

#  Exercise 5
# 1. get input as celsius
celsius = float(input("Enter a temperature in Celsius: "))
# 2. convert celsius to fah
fahrenheit = celsius * 1.8 + 32
# 3. print
print("The temperature is " + str(fahrenheit) + " in Fahrenheit.")
