#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:24:15 2018

@author: jin-tak.han
"""

# VARIABLE

watch = 10000
lighter = 10
print(watch + lighter) #10010

a = 'pig'
b = 'dad'
print(a+b) #pigdad


# LIST

family = ['mom', 'dad', 'sis', 'bro']
print(len(family)) #4
print(family[2])   #sis

family.remove('dad')
print(family) #['mom', 'sis', 'bro']


# WHILE

num = 1
while num <=100:
    print(num)
    num = num + 1 # 1....100
    
# FOR
    
family = ['mother', 'father', 'gentleman', 'sexy lady']

for x in family:
    print('%s %s' %(x, len(x)))

                # mother 6
                # father 6
                # gentleman 9
                # sexy lady 9
    
# IF
                
a = 10
b = 20

if a > b:
    print("a is bigger")
else:
    print("b is bigger") #b is bigger
    
    
# RANGE
    
print(list(range(2, 7))) # [2, 3, 4, 5, 6]


# FUNCTION
def plus(a,b):
    print(a+b)
    
plus(1,2)   #3

# RECURSIVE

def countDown(n):
    if n==0:
        print("done")
    else:
        print(n)
        countDown(n-1)

countDown(3)
                #3
                #2
                #1
                #done
                
                
# LOCAL, GLOBAL VARIABLES
    
globalVari = '01'
local = '06'

def method():
    local = '07'
    print ("local =", local)
    print ("globalVari =", globalVari)
    
method()    
# varia = 07
# globalVari = 01


# RETURN

def function(x):
    a = 3
    b = 4
    y = a * x + b
    print(y)
    return y

function(2)     #10

    
# LAMBDA

(lambda x,y: print(x + y))(10, 20)  #30

# MAP
# list(map(function, list))
list(map(lambda x: print(x ** 2), range(5)))
                                #[0, 1, 4, 9, 16]

# REDUCE
# reduce(func, order_data)
from functools import reduce        
reduce(lambda x, y: x + y, [0, 1, 2, 3, 4]) # 10
reduce(lambda x, y: y + x, 'abcde')         # 'edcba'

# FILTER
list(filter(lambda x: x < 5, range(10)))  #[0, 1, 2, 3, 4]


# SEQUENCE
x = 'banana'
print(x[0])     #b
print(x[1:])    #anana

#   x[0] = 'n'  cannot change

prime = [2,3,7,11]
prime.append(5)
print(prime) #[2, 3, 7, 11, 5]
prime.sort()
print(prime) #[2, 3, 5, 7, 11]

del prime[4]
print(prime) #[2, 3, 5, 7]

prime[0] =1
print(prime) #[1, 3, 5, 7]


characters = []
sentence = 'Be happy!'
for char in sentence:
    characters.append(char)
    
print(characters)
#['B', 'e', ' ', 'h', 'a', 'p', 'p', 'y', '!']

     
# TUPLE ()
a = 10
b = 20
temp = a
a = b
b = temp
print (a, b)    #20 10

c = 10
d = 20
c ,d = d, c
print (c, d)     #20 10
    
one = 5,
print(one)

p = (1,2,3)
q = p[:1] + (5,) + p[2:]
print(q)    #(1, 5, 3)
    

# TUPLE to LIST
p = (1, 2, 3)
q = list(p)
print(q)    #[1, 2, 3]

r = tuple(q)
print(r)    #(1, 2, 3)


# DICTIONARY
dic = {}
dic['dictionary'] = '1. A reference book...'
dic['python'] = 'Any of variouse..'

print(dic['python']) #Any of variouse..
del dic['python']
#print(dic['python'])  error

family = {'boy':'choi', 'girl':'kim', 'baby':'choi'}
print(family)           #{'boy': 'choi', 'girl': 'kim', 'baby': 'choi'}
print(family.keys())    #dict_keys(['boy', 'girl', 'baby'])
print(family.values())  #dict_values(['choi', 'kim', 'choi'])

print('boy' in family)  #true

    
# MODULE
import math
print(math.pi)  #3.141592653589793

import calendar
print(calendar.prmonth(2018,9))
    
#   September 2018
#Mo Tu We Th Fr Sa Su
#                1  2
# 3  4  5  6  7  8  9
#10 11 12 13 14 15 16
#17 18 19 20 21 22 23
#24 25 26 27 28 29 30

#import string
#print(string.capitalize('python'))
#print(string.replace('simple', 'i', 'a'))
#print(string.split('break into words'))
    
import random
print(random.random()) # 0~1

abc = ['a', 'b', 'c', 'd', 'e']
random.shuffle(abc)
print(abc)  #['b', 'a', 'e', 'd', 'c']

print(random.choice(abc))   #b


# FILE READ

f = open('/Users/jin-tak.han/Downloads/test.txt')
print(f.read())

        #test
        #
        #Alex

# FILE WRITE
letter = open('/Users/jin-tak.han/Downloads/test.txt', 'w')
letter.write("asd")
letter.close

letter = open('/Users/jin-tak.han/Downloads/test.txt', 'a+')
print(letter.read())    #asd

# READ FILE ONE LINE EACH
f = open('/Users/jin-tak.han/Downloads/test.txt')
print(f.readline())


# PICKLE GLOB OS.PATH
#users = {'kim':'3kid9', 'sun80':'393948', 'ljm':'py90390'}
#f = open('/Users/jin-tak.han/Downloads/test.txt', 'w')
#import pickle
#pickle.dump(users,f)
#f.close()


# OOP

# CLASS
class Amazon:
    strength = 20
    dexterity = 25
    vitality = 20
    energy = 15
    
    def attack(self):
        return 'Jab!!!'
    
    def exercise(self):
        self.strength += 2
        self.dexterity += 3
        self.vitality += 1
        
# save as diablo.py
#import diaplo
#jane = diablo.Amazon()
        
jane = Amazon()
print(jane.strength)    #20

john = Amazon()
print(john.strength)    #20
john.exercise()
print(john.strength)    #22


# INHERATANCE
class Person:
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2
    arms = 2
    legs = 2

    def eat(self):
        print('chap chap')

    def sleep(self):
        print('zzZZ...')

    def talk(self):
        print('blar...')
        
        

class Student(Person):     
    def study(self):
        print('hard...')
        
        
alex = Student()
alex.eat()
alex.study()

#chap chap
#hard...

# INITIALIZER
class Book:
    
    def __init__(self, title, price, author):
        self.setData(title, price, author)

    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print ('title : ', self.title)
        print ('price : ', self.price)
        print ('author : ', self.author)

        
a = Book('hi',200,'Alex')  #NEW book made~
a.printData()
#        title :  hi
#        price :  200
#        author :  Alex
        
        
        
        















