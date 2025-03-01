file=open("file handling.txt", "r")
for i in file:
    print(i)

#method 2
file=open("file handling.txt", "r")
print(file.read())

#method 3
file=open("file handling.txt", "r")
print(file.read(9))

#method 4
with open("file handling.txt", "r") as file:
    line=file.readlines()
    for i in line:
        word=i.split()
        print(word)

#writing on the file
file=open("file handling.txt", "w")
file.write("i have a dog \n")
file.write("my dogs name is toffee \n")
file.close()

#appending the file
file=open("file handling.txt", "a")
file.write("hello \n")
file.write("i am amelia")
file.close()