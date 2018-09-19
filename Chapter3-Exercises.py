# Exercise 1 and 2
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    if hours > 40:
        print("Pay:", hours * rate * 1.5)
    else:
        print("Pay:", hours * rate)
except:
    print("Error, please enter numeric input")


# Exercise 3
try:
    score = float(input("Enter your score: "))
    if score > 1 or score < 0:
        print("Bad score")
    elif 0.9 <= score <= 1.0:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")

except:
    print("Bad score")


