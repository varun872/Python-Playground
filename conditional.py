var1=6
var2=56
var3=int(input("Enter your number: "))
if var3>var2:
    print("Greater")
elif var3>var1 and var3<var2:
    print("In between")
else:
    print("Lesser")
    
# '=' assignment operator
# '==' comparision operator

age=int(input("Enter your age: "))
if age>18 and age<101:
    print("You are eligible to drive")
elif age<18 and age>7:
    print("You are not eligible to drive")
elif age==18:
    print("You are 18 and hence we cannot decide")
else:
    print("Invalid age")
