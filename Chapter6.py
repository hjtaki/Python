# String (str) - a sequence of characters

# len(str) - returns the number of characters
# my_str[index] - get character at index
# my_str[start:end] - a substring of my_str from start <= index < end

# Operators
# str1 + str2 : combine two strings ( concatenate )
# str * int : repeat str * int number of times
# str1 in str2 : return True if str1 is in str2

my_str = "Hello"

# how many 'l's are in my_str?
count = 0
for ch in my_str:
    if ch == "l":
        count += 1
print(count)

i = 0
count = 0
while i < len(my_str):
    if my_str[i] == "l":
        count += 1
    i += 1


# String Methods

# 1. converting case: lower(), upper(), capitalize()
print("BANANA".lower())
print("banana".upper())
print("banana".capitalize())

# 2. check identity of str: isalnum(), isdigit(), isalpha(), startswith(), find(), index()
print("banana1".isalnum())
print("123".isdigit())

st = "Kiwi"
if st.startswith("Ki"):
    print("Is is Kiwi?")

print("find(): ", st.find("i", 2))
print("index(): ", st.index("w"))

# 3. join(), split(), strip()
# str.strip(): strips off white-spaces
print("abc ".strip() + "def")

# str.split(sep): splits a str into a lnist using sep char
message = "Vancouver is always raining."
l = message.split(" ")  # ["Vancouver", "is", "always", "raining"]

# str.join(list): joins a list into a string with str
print(" * ".join(l))


# 4. count()
print("Banana".count("n"))


# Formatting a str
def pretty_message(first, last, city):
    std_info = "Firstname: {last}, Lastname: {first}, City: {city}".format(first=first, city=last, last=city)
    print(std_info)

pretty_message("John", "Smith", "Calgary")

grade = "Student_id: {}, Final_grade: {}".format(123, 100)
grade2 = "Student_name: %s, Final_grade: %d" % ("Derrick", 90)
print(grade)

