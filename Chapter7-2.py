# For more info https://docs.python.org/3/tutorial/inputoutput.html

filename = input("Enter a filename: ")
try:
    fhand = open(filename + ".txt", "r")
    output_file = open("output.txt", "w")
    # why does this code have newlines?
    for line in fhand:
        line = line.strip()
        if line.startswith("From:") and "berkeley" in line:
            output_file.write(line + "\n")

    fhand.close()
    output_file.close()
except:
    print("Invalid file name.")


# split() vs strip()
# 1. strip() -> str
a = " abcd \n".strip()  # "abcd"

# 2. split() : splits a string into a list
b = "hello world"
b.split(" ")  # ["hello", "world"]

c = "hello\nworld"
c.split("\n")  # ["hello", "world"]

