# Iteration (Repeat)

# 1. while - loop
# while <<condition(boolean expression>>:
#     << code to repeat>>
# it will repeat the code inside while loop while the condition is true.

#count = 0
#while count < 10:
#    print("Hello")
#    count += 1


# infinite loop - loop that never stops

#n = 0
#while True:
#     print("Hello")
#     n += 1
#     if n == 10:
#         break

'''
n = int(input("Enter a number: "))
count = 0

while count <= n:
     count += 1
     if count % 2 != 0:  # count is odd?
         continue
     else:
         print(count)'''


# 'continue' statement - skip to the next iteration
# 'break' statement breaks the loop (stops the loop)


# 2. for - loop
# syntax: for __loop var__ in __collection__:
#             << code to repeat >>

count = 0
for i in "HelloWorld":
    if i == "o":
        count += 1
        print(count)
print("---")

for i in range(10):  # 0, 1, 2, ..., 9
      if i % 2 == 0:
         print(i)
print("1---")


for i in range(2, 8):  # 2, 3, 4, 5, 6, 7
     print(i)
print("2---")


for i in range(1, 100, 5):  # 1, 6, 11, 16, ..., < 100
     print(i)
print("3---")

# range([start=0,] end[, steps=1]) : a sequence of numbers
# start <=    < end


for abcde in "aaabbb":
    print(abcde)
#
#
for i in ["Hello", "Hola", "Hi", 10, 100]:
    print(i)
print("4---")



friends = ["Joseph", "Glenn", "Sally"]
for friend in friends:
    print("Happy New Year,", friend)
    print("Done")
print("5---")



std_id = [11, 23, 34, 41, 5, 67, 12, 543, 31, 1235, 3221, 53]
count = 0
for id in std_id:
    if id % 3 == 0:
        print(id)
        count += 1
        print(count)


