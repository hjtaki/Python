# Exercise 1
count = 0
total = 0
while True:
    try:
        n = input("Enter a number: ")
        if n == "done":
            break
        total += int(n)
        count += 1
    except:
        print("Invalid input.")


print(total, count, total / count)


# Exercise 2
# first-way
l = []
while True:
    # get input
    n = input("Enter a number: ")
    if n.isdigit():
        # add it to my list
        l.append(int(n))
    else:
        break

maximum = max(l)
minimum = min(l)
average = sum(l) / len(l)
print("Max:", maximum, "Min:", minimum, "Avg", average)

# second-way
count = 0
total = 0
maximum = None
minimum = None
while True:
    try:
        n = input("Enter a number: ")
        if n == "done":
            break
        total += int(n)
        count += 1

        if minimum is None or int(n) < minimum:
            minimum = int(n)
        if maximum is None or int(n) > maximum:
            maximum = int(n)

    except:
        print("Invalid input.")

print("Max:", maximum, "Min:", minimum, "Avg", total / count)
