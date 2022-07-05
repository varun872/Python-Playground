a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
op=input("Enter what operation you what to perform: ")
if op=='*':
    if a==45 and b==3:
        print('555')
    else:
        print(a*b)
elif op=='+':
    if a==56 and b==9:
        print('77')
    else:
        print(a+b)
elif op=='/':
    if a==56 and b==6:
        print('4')
    else:
        print(a/b)
elif op=='-':
    print(a-b)
else:
    print("Invalid Operator entered!!")
