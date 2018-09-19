score = 0
answer1 = input("What is 1 + 1? ")

if not answer1 == "2":
    print("Correct!")
    score += 1
else:
    print("Wrong!")


answer2 = input("Who is the president of the usa? ")

# boolean operators
# 1. A and B: both A and B have to be true
# 2. A or B: either A or B has to be true
# 3. not A: a compliment of A

if answer2 == "Donald Trump" or answer2 == "donald trump":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")


print("Total Score: ", score)


# What is the difference?
# 1-conditional statement vs 4-conditional statements
# a = 10
#
# if a > 5:
#     print("Y")
# elif a > 7:
#     print("Y")
# elif a > 3:
#     print("Y")
# else:
#     print("N")
#
# if a > 5:
#     print("Y")
# if a > 7:
#     print("Y")
# if a > 3:
#     print("Y")
# if a > 6:
#     print("Y")




