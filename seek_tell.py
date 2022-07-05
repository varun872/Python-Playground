f=open("varun.txt")
print(f.tell()) #tells where "f" is currently
print(f.readline())
f.seek(15) #we are setting the file pointer to the location of our choice
print(f.tell())
print(f.readline())
print(f.tell())
