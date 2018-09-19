fp = open("mbox-short.txt", "r")

# prints all contents
# for line in fp:
#     print(line)

# 1. how many lines are in the txt file?
# count = 0
# for line in fp:
#     count += 1
#
# print("lines:", count)

whole = fp.read()  # read file content into a single string

print(len(whole))  # the number of characters

# 2. what is the first line of this text file?
lines = whole.split("\n")
print("First line=>", lines[0])

# 3. how many words are in the txt file?
words = whole.split(" ")
print(len(words), "words")

# 4. what is the first word of this txt file?
print(words[0])  # From

# 5. print all the lines that start with "From: "
for line in lines:
    if line.startswith("From:"):
        print(line)
