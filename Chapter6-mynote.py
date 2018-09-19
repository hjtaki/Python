my_str="Hello"
a=my_str[0]
print(a) #H


# len(str) - returns the number of charaters
# my_str[index] - get character ar index
# my_str[1:1] - a substring of my_str from 1 to 1
# Operators
# str + str : combine two strings( concatenate,combine)
# Str * int : repeat str * int numver of times
# Str1 in str2 : return True if str 1 is in str2

fruit="Banana"
b=fruit[0] #B


"T" + fruit[1:] #Tanana


#How many ls in my_str?
count=0
for ch in my_str:
    if ch =="l":
        count += 1
print(count)


i=0
while i < len(my_str):
    if my_str[i] =="l":
        count +=1
    i += 1

# use google documents to see all functions

print("BANANA".lower())
print("banana".upper())
print("banana".capitalize)

print("banana1".isalnum())
print("123".isdigit())


"asdasf".capitalize()


# those are just convertin way, let's see more useful way

# join split strip
print("abs ".strip()+"def") #abcdef - remove white space(blank and empty line

# str.split(sep) : splits a str into a list using sep char
message = "Vancouver is always raining."
l=message.split(" ")
print(l)            #['Vancouver', 'is', 'always', 'raining.']

# join : joins a list into a string with str

print("*".join(l))  #Vancouver*is*always*raining.

# startswith()
st = "Kiwi"
if st.startswith("Ki"):
    print("is it Kiwi?")


print("find():", st.find("i"))  #find(): 1
print("find():", st.find("i",2))  #find(): 3


# 4. count
print("Banana".count("n"))  #2

# Formatting a str
std_info1="Firstname: Derrick, Lastname:Park, City : Vancouver"
std_info2="Firstname: Alex, Lastname:Han, City : Vancouver"

std_info="Firstname: {}, Lastname:{}, City : {}".format("derrick","Part","Vancouver")
print(std_info) #Firstname: derrick, Lastname:Part, City : Vancouver


def pretty_message(first,last,city):
    std_info = "Firstname: {}, Lastname:{}, City : {}".format(first,last,city)
    print(std_info)

pretty_message("JT","han","Van")    #Firstname: JT, Lastname:han, City : Van

grade="Stdent_id:{}, final_grada : {}".format(123,100)
print(grade)        #Stdent_id:123, final_grada : 100

grade2="Stdent_name:%s, final_grada : %d" %("alex",90)
print(grade2)   #Stdent_name:alex, final_grada : 90


#compare
"Apple"<"Banana" # True


'''
mkdir
cat - show the contents

android-4a0d14c8d3943640:HAN ALEX_HAN$ cp myfile.py myfile2.py
android-4a0d14c8d3943640:HAN ALEX_HAN$ ls
myfile.py       myfile2.py
android-4a0d14c8d3943640:HAN ALEX_HAN$ mkdir python_files
android-4a0d14c8d3943640:HAN ALEX_HAN$ ls
myfile.py       myfile2.py      python_files
android-4a0d14c8d3943640:HAN ALEX_HAN$ mv myfile1.py python_files/
mv: rename myfile1.py to python_files/myfile1.py: No such file or directory
android-4a0d14c8d3943640:HAN ALEX_HAN$ mv myfile1.py python_files/
mv: rename myfile1.py to python_files/myfile1.py: No such file or directory
android-4a0d14c8d3943640:HAN ALEX_HAN$ ls
myfile.py       myfile2.py      python_files
android-4a0d14c8d3943640:HAN ALEX_HAN$ mv *.py python_files/
android-4a0d14c8d3943640:HAN ALEX_HAN$ ls
python_files
android-4a0d14c8d3943640:HAN ALEX_HAN$


android-4a0d14c8d3943640:HAN ALEX_HAN$ cd python_files
android-4a0d14c8d3943640:python_files ALEX_HAN$ ls
myfile.py       myfile2.py
android-4a0d14c8d3943640:python_files ALEX_HAN$ rm myfile.py
android-4a0d14c8d3943640:python_files ALEX_HAN$ ls
myfile2.py
android-4a0d14c8d3943640:python_files ALEX_HAN$


android-4a0d14c8d3943640:HAN ALEX_HAN$ ls
python_files
android-4a0d14c8d3943640:HAN ALEX_HAN$ rm -r python_files/
android-4a0d14c8d3943640:HAN ALEX_HAN$ ls
HAN
android-4a0d14c8d3943640:Desktop ALEX_HAN$ ls -l
total 0
drwxr-xr-x  3 ALEX_HAN  staff  102  8 Jan 11:47 HAN

android-4a0d14c8d3943640:Desktop ALEX_HAN$ whoami
ALEX_HAN

android-4a0d14c8d3943640:Desktop ALEX_HAN$ man ls


LS(1)                     BSD General Commands Manual                    LS(1)

NAME
     ls -- list directory contents

SYNOPSIS
     ls [-ABCFGHLOPRSTUW@abcdefghiklmnopqrstuwx1] [file ...]

DESCRIPTION
     For each operand that names a file of a type other than directory, ls
     displays its name as well as any requested, associated information.  For
     each operand that names a file of type directory, ls displays the names
     of files contained within that directory, as well as any requested, asso-
     ciated information.

     If no operands are given, the contents of the current directory are dis-
     played.  If more than one operand is given, non-directory operands are
     displayed first; directory and non-directory operands are sorted sepa-
     rately and in lexicographical order.

     The following options are available:

/long -> find function



android-4a0d14c8d3943640:HAN ALEX_HAN$ vim touch text_file.txt
2 files to edit

1. this is a popular linux text, code editor called vim
2.
3. there are many text editors that come with Unix -like operating system.


~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
-- INSERT --
android-4a0d14c8d3943640:HAN ALEX_HAN$


android-4a0d14c8d3943640:/ ALEX_HAN$ ls -l
total 45
drwxrwxr-x+ 46 root  admin  1564  8 Jan 08:52 Applications
drwxr-xr-x+ 61 root  wheel  2074  2 Oct 13:25 Library
drwxr-xr-x@  2 root  wheel    68 25 Feb  2016 Network
drwxr-xr-x@  4 root  wheel   136  4 Jan 12:41 System
drwxr-xr-x   9 root  admin   306  8 Jan 08:41 Users
drwxrwxrwt@  3 root  admin   102  8 Jan 11:24 Volumes
drwxr-xr-x@ 39 root  wheel  1326  4 Jan 12:41 bin
drwxrwxr-t@  2 root  admin    68 25 Feb  2016 cores
dr-xr-xr-x   3 root  wheel  4119  8 Jan 08:34 dev
lrwxr-xr-x@  1 root  wheel    11 25 Aug 17:15 etc -> private/etc
dr-xr-xr-x   2 root  wheel     1  8 Jan 08:35 home
-rw-r--r--@  1 root  wheel   313  2 Aug  2015 installer.failurerequests
dr-xr-xr-x   2 root  wheel     1  8 Jan 08:35 net
drwxr-xr-x@  6 root  wheel   204 25 Aug 17:17 private
drwxr-xr-x@ 59 root  wheel  2006  4 Jan 12:41 sbin
lrwxr-xr-x@  1 root  wheel    11 25 Aug 17:15 tmp -> private/tmp
drwxr-xr-x@ 13 root  wheel   442  2 Oct 13:26 usr
lrwxr-xr-x@  1 root  wheel    11 25 Aug 17:16 var -> private/var


android-4a0d14c8d3943640:/ ALEX_HAN$ ls -la             #hidden files
total 173
drwxr-xr-x  30 root  wheel   1088  4 Jan 12:39 .
drwxr-xr-x  30 root  wheel   1088  4 Jan 12:39 ..
-rw-rw-r--   1 root  admin      0 25 Feb  2016 .DS_Store
d--x--x--x   9 root  wheel    306  8 Jan 08:35 .DocumentRevisions-V100
drwx------   5 root  wheel    170 25 Aug 17:25 .Spotlight-V100
d-wx-wx-wt   2 root  wheel     68 25 Aug 16:31 .Trashes
----------   1 root  admin      0 25 Feb  2016 .file
drwx------  23 root  wheel    782  8 Jan 11:37 .fseventsd
-rw-------   1 root  wheel  65536 25 Aug 17:23 .hotfiles.btree
drwxr-xr-x@  2 root  wheel     68  1 Aug  2015 .vol
drwxrwxr-x+ 46 root  admin   1564  8 Jan 08:52 Applications
drwxr-xr-x+ 61 root  wheel   2074  2 Oct 13:25 Library
drwxr-xr-x@  2 root  wheel     68 25 Feb  2016 Network
drwxr-xr-x@  4 root  wheel    136  4 Jan 12:41 System
drwxr-xr-x   9 root  admin    306  8 Jan 08:41 Users
drwxrwxrwt@  3 root  admin    102  8 Jan 11:24 Volumes
drwxr-xr-x@ 39 root  wheel   1326  4 Jan 12:41 bin
drwxrwxr-t@  2 root  admin     68 25 Feb  2016 cores
dr-xr-xr-x   3 root  wheel   4119  8 Jan 08:34 dev
lrwxr-xr-x@  1 root  wheel     11 25 Aug 17:15 etc -> private/etc
dr-xr-xr-x   2 root  wheel      1  8 Jan 08:35 home
-rw-r--r--@  1 root  wheel    313  2 Aug  2015 installer.failurerequests
dr-xr-xr-x   2 root  wheel      1  8 Jan 08:35 net
drwxr-xr-x@  6 root  wheel    204 25 Aug 17:17 private
drwxr-xr-x@ 59 root  wheel   2006  4 Jan 12:41 sbin
lrwxr-xr-x@  1 root  wheel     11 25 Aug 17:15 tmp -> private/tmp
drwxr-xr-x@ 13 root  wheel    442  2 Oct 13:26 usr
lrwxr-xr-x@  1 root  wheel     11 25 Aug 17:16 var -> private/var
android-4a0d14c8d3943640:/ ALEX_HAN$

android-4a0d14c8d3943640:/ ALEX_HAN$ echo hello
hello


'''
