l = []
# while user types number
while True:
    # get input
    n = input("Enter a number: ")
    if n.isdigit():
        # add it to my list
        l.append(int(n))
    else:
        break

print(l)