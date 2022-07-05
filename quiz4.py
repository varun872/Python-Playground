n=int(input("Enter the number of rows: "))
boo=int(input("Enter 0 or 1: "))
if boo==1:
    for i in range(1,n+1):
        print(i*"*")
elif boo==0:
    for i in range(n,0,-1):
        print(i*"*")
else:
    print("Boo is not 0 or 1")
