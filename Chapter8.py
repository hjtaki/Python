fp=open("result.txt","r")
aa=fp.read()
bb=aa.split("\n")
print(bb)


print(1+3)

for line in bb:
    if line.startswith("X-DSPAM-C"):
        print(line)




print(1+3)