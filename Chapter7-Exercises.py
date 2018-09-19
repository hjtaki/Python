# Exercise 1
# fhand = open("mbox-short.txt", "r")
# for line in fhand:
#     print(line.strip())
#
# fhand.close()

# Exercise 2
# fname = input("Enter the file name: ")
# fhand = open(fname, "r")
# spam = 0
# count = 0
# for line in fhand:
#     if line.startswith("X-DSPAM-Confidence:"):
#         count += 1
#         spam += float(line.split()[1])
#
# fhand.close()
# print("Average spam confidence:", spam / count)

# Exercise 3
# fname = input("Enter the file name: ")
# if fname == "na na boo boo":
#     print("NA NA BOO BOO TO YOU - You have been punk'd!")
# else:
#     try:
#         fhand = open(fname, "r")
#         count = 0
#         for line in fhand:
#             count += 1
#         print("There were {} subject lines in ".format(count) + fname)
#
#     except FileNotFoundError:
#         print("File cannot be opened: " + fname)
