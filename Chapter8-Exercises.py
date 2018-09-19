# Exercise 1:

def chop(alist):
    alist.remove(alist[0])
    alist.remove(alist[len(alist)-1])


def middle(alist):
    return alist[1:len(alist)-1]


# Exercise 2:
# fhand = open("mbox-short.txt")
# count = 0
# for line in fhand:
#     words = line.split()
#     if len(words) == 0: continue
#     if words[0] != "From": continue
#     if len(words) >= 3: continue  # in case, words[2] doesn't exist
#     print(words[2])


# Exercise 3:
# fhand = open("mbox-short.txt")
# count = 0
# for line in fhand:
#     words = line.split()
#     if len(words) < 3 or words[0] != "From": continue
#     print(words[2])


# Exercise 4
# fhand = open("romeo.txt", "r")
# total_words = []
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in total_words:
#             total_words.append(word)
#
# fhand.close()
# total_words.sort()
# print(total_words)


# Exercise 5
# filename = input("Enter a file name: ")
# fhand = open(filename, "r")
# count = 0
# for line in fhand:
#     words = line.split()
#     if len(words) < 3 or words[0] != "From": continue
#     count += 1
#     print(words[1])
#
# print("There were {} lines in t he file with From as the first word".format(count))

# Exercise 6
# l = []
# while True:
#     # get input
#     n = input("Enter a number: ")
#     if n.isdigit():
#         # add it to my list
#         l.append(int(n))
#     elif n == "done":
#         break
#
# maximum = max(l)
# minimum = min(l)
#
# print("Maximum:", float(maximum))
# print("Minimum:", float(minimum))
