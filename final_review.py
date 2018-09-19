# variables, expressions, statements

# 1. variable : storage
abc1 = 10

# 2. data types
# int, float, bool
# str, list, dict

# (byte, set, tuple)

# 3. operators
# +, -, *, /, //, %, **
# ==, >, <, <=, >=

# 4. user input
# input(prompt) - returns the user input as str


# Chapter 3 - Conditional Statements
# a = 10
# b = 11
# c = 0
# if a == 10:
#     c += 1
# elif a >= 10:
#     c += 2
# else:
#     c += 3

# a = 10
# c = 0
# if a == 10:
#     c += 1
#     if a >= 10:
#         c += 1
# elif a > 10:
#     c += 2
# else:
#     c += 3
# print(c)

a = 0
b = 10
# logical operators: and, or, not
if a != 10 or b == 10:
    print()


# function: input -> output
def welcome_message():
    print("Hello")
    print("Hi")


# welcome_message()

# fruitful function
def add_three(a, b, c):
    return a + b + c

# non fruitful (void) func
def add_three2(a, b, c):
    print(a + b + c)


result1 = add_three(1, 2, 3)
print(result1)


import random
a = random.randint(1, 10)
print(a)


# Chapter 5: Iteration

# *1. while loop
# a = 0
# while a < 10:
#     print(a)
#     a += 1

# example question
# 1. get user input as an int
# 2. print all even numbers from 0 <= to <= user input

# n = int(input())
# a = 0
# while a <= n:
#     if a % 2 == 0:
#         print(a)
#     a += 1
#
# # *2. for loop
# n = int(input())
# for i in range(n+1):
#     if i % 2 == 0:
#         print(i)


# Q. FizzBuzz
# Integers from 0 to (<=user_input)

# print 'Fizz' if the number is a multiple of 3
# print 'Buzz' if the number is a multiple of 5
# print 'FizzBuzz' if the number is a multiple of 3 and 5
# else print the number


int(input("Enter number :"))
for n range(0,input+1):
    if n % 15=0:
        print("FizzBuzz")
    elif n % 3 =0:
        print("Fizz")
    elif n% 5 =0:
        print("Buzz")
    else:
        print(n)

int(input("Enter number :"))
n=0
while n<=15:
    if n % 15=0:
        print("FizzBuzz")
    elif n % 3 =0:
        print("Fizz")
    elif n % 5 =0:
        print("Buzz")
    else:
        print(n)
    n+=1


# ex)
# input : 15
# output:
        # 1
        # 2
        # Fizz
        # 4
        # Buzz
        # Fizz
        # 7
        # 8
        # Fizz
        # Buzz
        # 11
        # Fizz
        # 13
        # 14
        # FizzBuzz

# for - loop
n = int(input())
for i in range(1, n+1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# while - loop
n = int(input())
c = 1
while c <= n:
    if c % 3 == 0 and c % 5 == 0:
        print("FizzBuzz")
    elif c % 3 == 0:
        print("Fizz")
    elif c % 5 == 0:
        print("Buzz")
    else:
        print(c)

    c += 1


# Chapter 6 - Strings
# str - a sequence of chars, immutable
a = "abcd"
# a[0] -> "a"
# a[0:2] -> "ab"
# len(a) -> 4

# a.count("a")  #1
# a.index("c")  #2
# a.upper()     #ABCD
asd= a.isdigit()
print(asd)

# Chapter 8 - Lists
# str - a sequence of items, mutable
# a = ["a", "b", "c", "d"]
# a[0] -> "a"
# a[0:2] -> ["a", "b"]
# len(a) -> 4

# a.append("d")
# a.pop()
# a.remove("b")
# a.count("a")
# a.index("c")
# ...
