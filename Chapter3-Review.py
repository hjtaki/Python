# Conditional execution

# 1. Boolean Expressions
print(3 == 3)
# ==, !=, >, <, >=, <=
print(3 != 3)

# is, is not
print(3 is not 3)
print(3 is 3.0)  # False
print(3 == 3.0)  # True
print("-----------")

# 2. Logical Operators: and, or, not
a = 10
print(a > 5 and a > 11)  # False
print(a > 5 or a > 11)  # True
print(not a > 5)  # False
print("-----------")

# 3. Conditional Statements
if a == 0 or a == 10:
    print("YYES")
print("-----------")

# - Chained Conditionals
city = "Cal"
if city == "Van":
    print("Vancouver")
elif city == "Edm":
    pass
elif city == "Brn":
    print("Burnaby")
elif city == "Cal":
    pass
elif city == "Tor":
    print("Toronto")
else:
    print("Not a Canadian City")
print("-----------")

# - Nested conditionals
x = 7
y = 10

if x == y:
    print("x is equal to y")
else:
    if x > y:
        print("x is greater than y")
    else:
        print("y is greater than x")

print("4-----------")
# 4. Even number? 0, 2, 4, 6, 8 ...
#    Odd number? 1, 3, 5, ...
n = 9
if n % 2 == 0:  # if n is divisible by 2
    print("Even")
else:
    print("Odd")


# 5. try? except? block
try:
    hours = int(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    print("Pay:", hours * rate)
except:
    print("Invalid input. Please enter a number.")

# 6. Short-circuit evaluation of logical expressions

x = 10
if x == 10 or x > 5:
    print("Yes")
else:
    print("123")


if x == 10 and x < 0:
    print("Yes")


x = 10
y = 0
# Guardian pattern - where we create a logical expression with
#                    additional comparisons to take take advantage of
#                    the short-circuit behaviour
if x > 5 and y != 0 and (x / y > 1):
    print("HEY YES")

















