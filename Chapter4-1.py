# Function - takes input and returns(generates) output


# Non-fruitful(void) function
def welcome_message():
    print("Welcome to Vancouver")
    name = input("What is your name? ")
    print("Hello " + name)


# welcome_message()
# welcome_message()
# print(welcome_message())  # None


# Fruitful function
def add_two(a, b):
    c = a + b
    return c

print(add_two(1,2))


# Ticket price
def ticket_price(age):
    if age > 50:
        return 10
    elif 17 < age < 50:
        return 15
    else:
        return 9

print(ticket_price(28))

user_age = int(input("Enter your age: "))
price = ticket_price(user_age)
print("Your ticket price is $", price)


# Built-in functions: functions that are already built into python
# ex) print(), type(), len(), max(), min(), ...

# Type conversion functions: int, float, bool, str

# int(value)
# ex) int("101") -> 101
# ex) int(101.111) -> 101

# float(value)
# ex) float("10.1") -> 10.1
# ex) float("10") -> 10.0
# ex) float(10) -> 10.0

# str(value)
# ex) str(10) -> "10"
# ex) str(10.11) -> "10.11"
# ex) str("aa") -> "aa"





