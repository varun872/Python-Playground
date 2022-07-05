# i=0
# while(True):
#     if(i<5):
#         i+=1
#         continue #Don't execute the lines below until the condition becomes false
#     print(i,end=' ')
#     if(i==45):
#         break #stop the loop
#     i+=1
    
#Quiz
num=int(input("Enter your number: "))
while(num<100):
    num=int(input("Enter your number: "))
print("Congrats you entered a number greater than 100")

#With break and continue
while(True):
    no=int(input("Enter a number: "))
    if no>100:
        print("Congrats you entered a number greater than 100")
        break
    else:
        continue
