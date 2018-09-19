# Ex 1
my_str = "Banana"
i = len(my_str) - 1
while i >= 0:
    print(my_str[i])
    i -= 1

# Ex 2 - fruit[:] means the whole fruit string

# Ex 3
def count(string, letter):
    count = 0
    for ch in string:
        if ch == letter:
            count += 1

    return count

# Ex 4
print("banana".count("a"))


# Ex 5
str = "X-DSPAM-Confidence:0.8475"
print(float(str[str.find(":")+1:]))

# Ex 6 - Read the documentation.