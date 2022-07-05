# a=int(input("Enter the first number: "))
# b=int(input("Enter the second number: "))
# print("The sum is:",a+b)
# The above print statement will throw error if the input is not a 'int'

# print("Print this line please!!")
# If the 1st print has an error then the 2nd print won't be executed therefore we can use try and except

a=input("Enter the first number: ")
b=input("Enter the second number: ")
try:
    print("The sum is:",int(a)+int(b))
except Exception as e:
    print(e)
print("Print this line please!!")
