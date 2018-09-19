'''
8. list
string - immutable
list - mutable

len for list is the number of list elements

range

'''

l =["hello","hola","Hi"]

print(len(l))   #3
print(l[1])     #hola       index
print(l[:2])    #['hello', 'hola']      slice

for item in l:
    print(item)
    '''hello
        hola
        Hi'''


print(range(len(l)))    #range(0, 3) from 0 to 2

for i in range(len(l)): # 0 1 2
    print(l[i])
    '''hello
    hola
    Hi'''

## range(4) # 0,1,2,3


## Concatenating
a = ["1"]
b = ["2"]
print(a+b) #['1', '2']



## list Method( append, count, insert, pop,

    # append : adding list


l=[1,2,3]

print(type(l)) # <class 'list'>

print(dir(list))
            #['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(l.append(4))
print(l)            #[1, 2, 3, 4]

print(l.count(2))   # 1
print(l.index(2))   # 1

l.reverse()
print(l)            #[4, 3, 2, 1]

l.sort()
print(l)            #[1, 2, 3, 4] order alpabet

l.pop()
print(l)         #[1, 2, 3]

l.insert(1,5)     #[1, 5, 2, 3]
print(l)

l.extend([7,7]) #[1, 5, 2, 3, 7, 7]
print(l)

print(10 in l)  #False

print(len(l)) #6

print(max(l))   #7

print(min(l))   #1

print(sum(l)/len(l))    # 4.1 - average


aa= "a b c"
print(aa.split())   #['a', 'b', 'c']
print(aa)               # a b c
print(aa.split("b"))    #['a ', ' c']


