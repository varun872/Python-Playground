#File Basics
'''
Different Modes
r-for reading a file
w-for writing to a file(creates a file if file doesn't exist)
a-append at the end of the file
'''
# to read the text as a whole
# f=open("text.txt",'r') can also be written as:-
with open("varun.txt") as f
# content=f.read(3) reads the first 3 characters
# content=f.read(3) reads the next 3 characters
content=f.read() #reads all contents in the file
print(content)
f.close()

# to print line by line
f=open("text.txt",'r')
contents=f.readline() #reads 1 line at a time
contents1=f.readlines() #reads the whole text line by line and is stored in a list
print(contents)
print(contents1)
# for line in f:
#     print(line)
f.close()

# write to a file
f=open("varun.txt",'w') # varun.txt doesn't exist but using 'w' it is created
lenght=f.write("Varun is a good boy")
print(lenght) #prints the number of characters written
f.close()

# appending to a file
f=open("varun.txt",'a') 
f.write("Varun is a bad boy")
f.close()

# both read and write 
f=open("text.txt",'r+') 
contents2=f.read()
print(contents2)
f.write("Varun is a bad boy")
f.close()
