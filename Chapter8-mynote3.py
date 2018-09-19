'''

| : chained , and

NAME
       pipe - Postfix delivery to external command

SYNOPSIS
       pipe [generic Postfix daemon options] command_attributes...

DESCRIPTION
       The pipe(8) daemon processes requests from the Postfix queue manager to
       deliver messages to external commands.  This program expects to be  run
       from the master(8) process manager.

       Message  attributes such as sender address, recipient address and next-
       hop host name can be specified as command-line macros that are expanded
       before the external command is executed.

       The  pipe(8)  daemon  updates  queue files and marks recipients as fin-
       ished, or it informs the queue manager that delivery  should  be  tried
       again  at  a  later  time.  Delivery  status  reports  are  sent to the
       bounce(8), defer(8) or trace(8) daemon as appropriate.

SINGLE-RECIPIENT DELIVERY



cat/usr/share/dict/words|grep"ous$"
    : see words and find out
    : ends with ous
    : ^apple : starts with apple

wc-l/usr/share/dict/words
    : counts lines (-l)

cat/usr/share/dict/words|grep"ous$"|wc-l
    : count

ls-al/usr/share > ~/ls.txt
    : > :  put the results on the txt file

Nana:Desktop ALEX_HAN$ ls
HAN		words.txt
Nana:Desktop ALEX_HAN$ touch result.txt
Nana:Desktop ALEX_HAN$ ls
HAN		result.txt	words copy	words.txt
Nana:Desktop ALEX_HAN$ cat words.txt
asdasd
as
das
d
ask
a
pdf
as
das
d
asd
as
d
asdNana:Desktop ALEX_HAN$ cat words.txt | grep ^as$
as
as
as
Nana:Desktop ALEX_HAN$ cat words.txt | grep ^as
asdasd
as
ask
as
asd
as
asd
Nana:Desktop ALEX_HAN$ cat words.txt | grep ^as > result.txt
Nana:Desktop ALEX_HAN$ cat result.txt
asdasd
as
ask
as
asd
as
asd
Nana:Desktop ALEX_HAN$



Nana:Desktop ALEX_HAN$ ls
HAN		result.txt	words copy	words.txt
Nana:Desktop ALEX_HAN$ ls > result.txt
Nana:Desktop ALEX_HAN$ cat result.txt
HAN
result.txt
words copy
words.txt
Nana:Desktop ALEX_HAN$


less result.txt : new screen


nano~/ls.txt

nano : editor




PART3
https://gist.github.com/


3-1
Nana:Desktop ALEX_HAN$ history | grep cat | wc -l
      18
Nana:Desktop ALEX_HAN$ history | grep cat
   92  cat myfile.py
  143  cat text_file.txt
  150  cat Terminal\ Saved\ Output
  180  cat/usr/share/dict/words
  181  cat/usr/share/dict/words
  182  cat/usr/share/dict/words
  183  cat/usr/share/dict/words
  186  cat/usr/share/dict/words
  189  cat.words.txt
  191  cat words.txt
  200  cat/usr/share/dict/words.txt
  205  cat words.txt
  206  cat words.txt | grep ^as$
  207  cat words.txt | grep ^as
  208  cat words.txt | grep ^as > result.txt
  209  cat result.txt
  214  cat result.txt
  219  history | grep cat | wc -l
  220  history | grep cat
Nana:Desktop ALEX_HAN$


3-2


Nana:Desktop ALEX_HAN$ cat words.txt | grep ^a.*s$ | wc -l
       0
    . : any charater
    + : 0 or more
    * : 1 or more

3-4 unixcommand,download&save wevpage

wget
curl


Nana:Desktop ALEX_HAN$ curl https://www.canada.ca/en.html
<!doctype html>

<!--[if lt IE 9]>
<html class="no-js lt-ie9" dir="ltr" lang="en" xmlns="http://www.w3.org/1999/xhtml">
<![endif]-->
<!--[if gt IE 8]><!-->
<html class="no-js" dir="ltr" lang="en" xmlns="http://www.w3.org/1999/xhtml">
<!--<![endif]-->
    <head>

<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta charset="utf-8">


------------------------------------------------------------------------------------------

CHAPTER 7
- so far variables in RAM, persist data - > hard disk !


'''

fp=open("mbox-short.txt","r")
print(fp)   #<_io.TextIOWrapper name='mbox-short.txt' mode='r' encoding='UTF-8'>

# \n : new line : enter key

# pints all contents by lines
#for line in fp: # line not charater
#    print(line) # come out contents


# how many lines?
'''
count = 0
for line in fp:
    count +=1 # = count = count +1

print("lines:",count)   #lines: 1910
'''

# reading whole file

whole =fp.read()
print(whole)    # open the file and store to single string(whole variable) and read /
print(len(whole))   # 94626 including spaces, the numbers of characters

# what is the firsr line

lines = whole.split("\n")

print("first line :",lines[0])

# how many words in the txt files?

words = whole.split(" ")
print(len(words), "words")  #7727 words

# first word
print(words[0]) #From

# print all the lines that starts with from

for line in lines:
    if line[:5] ==("From:"):
        print(line)
                    # From: stephen.marquard@uct.ac.za ....
                    # From: stephen.marquard @ uct.ac.za


for line in lines:
    if line.startswith("From:"):
        print(line)

# if this for is occured in new file, there will be enpty lines

        # From: stephen.marquard@uct.ac.za

        # From: louis@media.berkeley.edu


# if we do SPLIT, it makes list ?? yes
    # print itself has a new line
    # if it has been splited, it became a line. -> if printed, become normal.

'''
for line in fhand:
    line = line.strip()                 # to remove enters
    if line.startswith("From:"):
        print(line)
'''


# split vs strip : remove new line
a = "abcd \n".strip()   #abcd
print(a)

b="hello world"
print(b.split())    #['hello', 'world']

c= "hello\nworld"
print(c.split())    #['hello', 'world']


for line in lines:
    if line[:5] ==("From:") and "cwen" in line:
        print(line)

'''From: cwen@iupui.edu
                  From: cwen@iupui.edu
                From: cwen@iupui.edu
                From: cwen@iupui.edu
                From: cwen@iupui.edu'''


# writing into a file


fhand1= open("mbox-short.txt","r")
output_file = open("output.txt","w")        # generated

for line in lines:
    if line[:5] == ("From:") and "cwen" in line:
        output_file.write(line+"\n")

fhand1.close()
output_file.close()

# if file name was wrong when opening the file
try:
    fhand = open("mbox-short.txt","r")
except:
    print("file not found")


fp.close()


