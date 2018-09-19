'''collections

1. list : a sequence of any data type(linear)
        [   ,   ,   ,]
    index 0    1   2
2. string : a seq of character
        " , ,   ,   " has index too



3. Dictionary(HashMap) (in a bag)
- collection, no sequence(key : value)
- able change the order
- d = {"a:b","c:d"}
d["a"]=b
d["1"]=error


'''

d = {"last":"Han","first":"JT"}
print(d["last"])    #han

print("last" in d) # True

print(d)        #{'last': 'Han', 'first': 'JT'}

d["english"] = "alex"
print(d)        #{'last': 'Han', 'first': 'JT', 'english': 'alex'}


print("asd\nasd")

#asd
#asd










article="""One of After a few confusing tweets, U.S. President Donald Trump on Thursday pushed the House
to renew a critical national security program that allows spy agencies to collect intelligence on foreign targets abroad""".lower()

d={}

words = article.split(" ")
print(words)        #['After', 'a', 'few', 'confusing', 'tweets,', 'U.S.', 'President', 'Donald', 'Trump', 'on',
                    # 'Thursday', 'pushed', 'the', 'House', 'to', 'renew', 'a', 'critical', 'national', 'security',
#                   'program', 'that', 'allows', 'spy', 'agencies', 'to', 'collect', 'intelligence', 'on', 'foreign', 'targets', 'abroad']


for word in words:
    if word in d:
        d[word] +=1
    else:
        d[word] =1

print(d)    #{'one': 1, 'of': 1, 'after': 1, 'a': 2, 'few': 1, 'confusing': 1, 'tweets,': 1, 'u.s.': 1,
            # 'president': 1, 'donald': 1, 'trump': 1, 'on': 2, 'thursday': 1, 'pushed': 1, 'the': 1, 'house\nto': 1,
#           'renew': 1, 'critical': 1, 'national': 1, 'security': 1, 'program': 1, 'that': 1, 'allows': 1, 'spy': 1, 'agencies': 1,
#           'to': 1, 'collect': 1, 'intelligence': 1, 'foreign': 1, 'targets': 1, 'abroad': 1}



article2="hello I have a pet. I want to hello learn".lower()
word2=article2.split(" ")
print(word2)        #['hello', 'i', 'have', 'a', 'pet.', 'i', 'want', 'to', 'hello', 'learn']

dic={}

for word1 in word2:
    if word1 in dic:
        dic[word1] +=1
    else:
        dic[word1] =1
print(dic)      #{'hello': 2, 'i': 2, 'have': 1, 'a': 1, 'pet.': 1, 'want': 1, 'to': 1, 'learn': 1}


for k in dic:
    print(k)


count=0
for k in dic.values():
    print(k)


for k,v in dic.items():
    print("key:",k , "value :",v)
'''
    key: hello
    value: 2
    key: i
    value: 2
    key: have
    value: 1
    key: a
    value: 1
    key: pet.value: 1
    key: want
    value: 1
    key: to
    value: 1
    key: learn
    value: 1'''
'''
review




'''