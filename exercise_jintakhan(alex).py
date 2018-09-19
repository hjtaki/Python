# CHAPTER 2

'''
Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
Enter your name: Chuck
Hello Chuck'''

#n=input("Enter your name : ",)
#print("Hellow",n)

'''
Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
We won’t worry about making sure our pay has exactly two digits after the decimal place for now. 
If you want, you can play with the built-in Python round function to properly round the resulting pay to two decimal places.'''


#h=float(input("enter hours : ", ))
#r=float(input("enter rate : ", ))
#print(r * h)

'''
Exercise 4: Assume that we execute the following assignment statements:
width = 17
height = 12.0
For each of the following expressions, write the value of the expression and the type (of the value of the expression).
1. width//2 
2. width/2.0 
3. height/3 
4. 1 + 2 * 5
Use the Python interpreter to check your answers.'''

# print(17//2)   # 8
# print(17/2.0)  # 8.5
# print(12.0/3)  # 4.0
# print(1+2*5)   # 11

'''
Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, 
and print out the converted temperature.'''

# n=int(input("Celsious temp : "),)
# print(n*1.8+32)



# CHAPTER3
'''
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0'''

# h=float(input("enter hours:",))
# r=float(input("enter rate:",))
#
# if h<=40:
#     print(h * r)
# else:
#     print(40*r+(h-40)*1.5*r)



'''
Exercise 2: Rewrite your pay program using try and except so that your pro-gram handles non-numeric input gracefully 
            by printing a message and exiting the program. The following shows two executions of the program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input'''


# try:
#     h = float(input("enter hours:", ))
#     r = float(input("enter rate:", ))
#
#     if h <= 40:
#         print(h * r)
#     else:
#         print(40 * r + (h - 40) * 1.5 * r)
#
# except:
#     print("please input numeric input")

'''
Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. 
            If the score is between 0.0 and 1.0, print a grade using the following table:
Score   Grade
>= 0.9  A   
>= 0.8  B
>= 0.7  C
>= 0.6  D
 < 0.6  F

Enter score: 0.95       A
Enter score: perfect    Bad score
Enter score: 10.0       Bad score
Enter score: 0.75       C
Enter score: 0.5        F

Run the program repeatedly as shown above to test the various different values for input.'''



# try:
#     s = float(input("score:", ))    # must put s inside try
#
#     if s >=0.9 and s<1.0:
#         print("A")
#     elif s>=0.8 and s<0.9:
#         print("B")
#     elif s>=0.7 and s<0.8:
#         print("C")
#     elif s>0.6 and s<0.7:
#         print("D")
#     elif s<0.6 and s>0:
#         print("F")
#     elif s>1 or s<0:
#         print("bad score")
#
# except:
#     print("bad score")


# Chapter 4
'''Exercise 1: Run the program on your system and see what numbers you get. 
                Run the program more than once and see what numbers you get.
                The random function is only one of many functions that handle random numbers. 
                The function randint takes the parameters low and high, and returns an integer between low and high (including both).
                The random module also provides functions to generate random values from con- tinuous distributions 
including Gaussian, exponential, gamma, and a few more.'''


#import random
# print(random.randint(5, 10))   #5
# print(random.randint(5, 10))  #9
#
# t = [1, 2, 3]
# print(random.choice(t))   #2
# print(random.choice(t))     #3





'''
Pulling together the code fragments from the previous section, the whole program looks like this:'''

# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')
#
#
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
#
# repeat_lyrics()



'''        
# Code: http://www.py4e.com/code3/lyrics.py
This program contains two function definitions: print_lyrics and repeat_lyrics. 
Function definitions get executed just like other statements, but the effect is to create function objects. 
The statements inside the function do not get executed until the function is called, and the function definition generates no output.
As you might expect, you have to create a function before you can execute it. 
In other words, the function definition has to be executed before the first time it is called.

Exercise 2: Move the last line of this program to the top, so the function call appears before the definitions. 
            Run the program and see what error message you get.'''


'''
Exercise 3: Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. 
            What happens when you run this program?'''


'''Exercise 4: What is the purpose of the “def” keyword in Python?
    a) It is slang that means “the following code is really cool”
    b) It indicates the start of a function
    c) It indicates that the following indented section of code is to be stored for later d) b and c are both true
    e) None of the above'''

'''
Exercise 5: What will the following Python program print out?'''

# def fred():
#     print("Zap")
#
# def jane():
#     print("ABC")
#
# jane()  # ABC
# fred()  # Zap
# jane()  # ABC


'''
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
create a function called computepay which takes two parameters (hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0'''

# def computepay(h,r):
#     if h <= 40:
#         print(h * r)
#     else:
#         print(40 * r + (h - 40) * 1.5 * r)
#
# computepay(45,10)


'''
Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade 
            that takes a score as its parameter and returns a grade as a string.
Score
>0.9 A 
>0.8 B 
>0.7 C 
>0.6 D 
<= 0.6 F

Program Execution:
Enter score: 0.95       A
Enter score: perfect    Bad score
Enter score: 10.0       Bad score
Enter score: 0.75       C
Enter score: 0.5        F

Grade
Run the program repeatedly to test the various different values for input.'''
#
# try:
#     def computegrade(s):
#         if s >=0.9 and s<1.0:
#             print("A")
#         elif s>=0.8 and s<0.9:
#             print("B")
#         elif s>=0.7 and s<0.8:
#             print("C")
#         elif s>0.6 and s<0.7:
#             print("D")
#         elif s<0.6 and s>0:
#             print("F")
#         elif s>1 or s<0:
#             print("bad score")
#         else:
#             print("bad score")
#
# except:
#     print("bad score")
#
# computegrade(0.95)
# computegrade(10.0)
# computegrade(0.75)
# computegrade(0.5)
# #computegrade("perfect")            ?? error


#Chapter5

'''
Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. 
            Once “done” is entered, print out the total, count, and average of the numbers. 
            If the user enters anything other than a number, detect their mistake
            using try and except and print an error message and skip to the next number.
            
Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333'''

#?????
'''
count=0
total=0

while True:
    n=(input("Enter a number : ",))
    if n == "done":
        break
    else:
        total += int(n)
        count += 1

print(total, count, total/count)


count=0
total=0

while True:
    try:
        n=input("Enter a number : ",)
        if n == "done":
            break
        else:
            total += int(n)
            count += 1

    except:
        print("Invali data")
print(total, count, total/count)

count=0
total=0
try:
    while True:
        n=input("Enter a number : ",)
        if n == "done":
            break
        else:
            total += int(n)
            count += 1

except:
        print("Invali data")
''''''print(total, count, total/count)


Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out 
            both the maximum and minimum of the numbers instead of the average.'''

# ???
#
# l=[]
# while True:
#     n= input("Enter a number")
#     if n.isdigit():
#         l.append(int(n))
#     else:
#         break
# m=max(l)
# n=min(l)
# a=sum(l)/len(l)
# print(m,n,a)



# Chapter 6

'''
Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards 
            to the first character in the string, printing each letter on a separate line, except backwards.
            Another way to write a traversal is with a for loop: 

            Each time through the loop, the next character in the string is assigned to the variable char. 
            The loop continues until no characters are left.'''

# for char in fruit:
# print(char)

# word="Apple"
# a= len(word)-1
# while a >=0:
#     print(word[a])
#     a -= 1



'''
Exercise 2: Given that fruit is a string, what does fruit[:] mean?'''


# for char in fruit:
#     print(char)

'''
Exercise 3:??
Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.'''

# def count(str,letter):
#     print(str[letter-1])
#
# count("apple",3)


# def count1(string,letter):
#     count1=0
#     for ch in string:
#         if ch == letter:
#             count1 +=1
#     return count1
#
# count1("apple",a)

'''
Exercise 4:
There is a string method called count that is similar to the function in the previous exercise. 
Read the documentation of this method at https://docs.python.org/3.5/library/stdtypes.html#string-methods 
and write an invocation that counts the number of times the letter a occurs in “banana”.'''

# a="apple"
# b=a.count("a")
# print(b)

'''?
Exercise 5: Take the following Python code that stores a string:‘
str = ’X-DSPAM-Confidence:0.8475’
Use find and string slicing to extract the portion of the string after the colon character 
and then use the float function to convert the extracted string into a floating point number.'''

str ="X-DSPAM-Confidence:0.8475"
# print(float(str[str.find(":")+1:]))
# print(float(str[str.find(":")+1:])) # 0.8475

'''
Exercise 6:
Read the documentation of the string methods at
https://docs.python.org/3.5/library/stdtypes.html#string-methods
You might want to experiment with some of them to make sure you understand how they work. 
strip and replace are particularly useful. The documentation uses a syntax that might be confusing. 
For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. 
So sub is required, but start is optional, and if you include start, then end is optional.'''


#CHapter7
'''
Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. 
Executing the program will look as follows:

python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
     SAT, 05 JAN 2008 09:14:16 -0500
You can download the file from
www.py4e.com/code3/mbox-short.txt'''

# fopne= open('/Users/jin-tak.han/CICCC/python/mbox-short.txt','r')
#
# for line in fopne:
#     line.rstrip()
#     print(line)
#
# fopen.close()

'''
Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
X-DSPAM-Confidence:0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. 
Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, 
print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.'''



'''
Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist. Here is a sample execution of the program:
FILES
python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt
python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
We are not encouraging you to put Easter Eggs in your programs; this is just an exercise.'''


#Chapter8

'''
Exercise 1: Write a function called chop that takes a list and modifies it, 
            removing the first and last elements, and returns None.
            Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.'''

# def chop(list):
#     list.remove(list[0])
#     list.remove(list[len(list)-1])
#
# abc=['a','b','c','d','e']
# print(chop(abc))    #None
#
#
# def middle(lista):
#     return(lista[1:len(lista)-1])
#
# abc1=['a','b','c','d','e']
# print(middle(abc1)) # b c d




'''?
Exercise 2: Figure out which line of the above program is still not properly guarded.
            See if you can construct a text file which causes the program to fail
            and then modify the program so that the line is properly guarded
            and test it to make sure it handles your new text file'''
#
# file=open("mbox-short.txt","r")
#
# count=0
# for line in file:
#     words=line.split()
#     if len(words) ==0:
#         continue
#     if words[0]!= "From":
#         continue
#     if len(words) >=3:
#         continue
#     print(words[2])


'''    ?        
Exercise 3: Rewrite the guardian code in the above example without two if statements.
            Instead, use a compound logical expression using the and logical operator with a single if statement'''

'''
Exercise 4: Download a copy of the file from www.py4e.com/code3/romeo.txt Write a program to open the file romeo.txt 
            and read it line by line. For each line, split the line into a list of words using the split function.
            For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list.
            When the program completes, sort and print the resulting words in alphabetical order.

Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']'''

# can't open txt, changed a little

# txt= "But soft what light through yonder window breaks It is the east and Juliet is the sun Arise fair sun and kill the envious moon Who is already sick and pale with grief"
#
# words=txt.split() #['But', 'soft', 'what', 'light', 'through', 'yonder', 'window', 'breaks', 'It', 'is', 'the', 'east', 'and', 'Juliet', 'is', 'the', 'sun', 'Arise', 'fair', 'sun', 'and', 'kill', 'the', 'envious', 'moon', 'Who', 'is', 'already', 'sick', 'and', 'pale', 'with', 'grief']
# l=[]
#
# for word in words:
#     if word not in l:
#         l.append(word)
# print(l)        #['But', 'soft', 'what', 'light', 'through', 'yonder', 'window', 'breaks', 'It', 'is', 'the', 'east', 'and', 'Juliet', 'sun', 'Arise', 'fair', 'kill', 'envious', 'moon', 'Who', 'already', 'sick', 'pale', 'with', 'grief']






'''?
Exercise 5: Write a program to read through the mail box data and when you find line that starts with “From”, 
            you will split the line into words using the split function. We are interested in who sent the message, 
            which is the second word on the From line.

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

            You will parse the From line and print out the second word for each From line, 
            then you will also count the number of From (not From:) lines and print out a count at the end.

This is a good sample output with a few lines removed:

python fromcount.py
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu

[...some output removed...]

ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word'''


fp=open("mbox-short.txt","r")
for line in fp:
    words =line.split()
    print(words)



# filename = input("Enter a file name: ")
# fhand = open(filename, "r")
# count = 0
# for line in fhand:
#     words = line.split()
#     if len(words) < 3 or words[0] != "From":
#         continue
#     count += 1
#     print(words[1])
#
# print("There were {} lines in the file with From as the first word".format(count))



'''
Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers 
            at the end when the user enters “done”. Write the program to store the numbers the user enters in a list 
            and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0'''

# l=[]
# while True:
#     n = input("input a list of numbers: ")
#     if n.isdigit():
#         l.append(int(n))
#     elif n == "done":
#         print("max:",max(l),"min:",min(l))
#         break
