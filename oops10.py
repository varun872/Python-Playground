class A:
    classvar1="I am a class variable in class A"
    def __init__(self):
        self.var1="Inside constructor of class A"
        self.classvar1="Instance var in class A"
        self.special="Special"

class B(A):
    classvar1="I am in class B" #overriding
    def __init__(self):
        #super().__init__()
        self.var1="Inside constructor of class B"
        self.classvar1="Instance var in class B" #has been overwritten. We cannot use the constructor to access A anymore
        super().__init__()

a=A()
b=B()

print(b.classvar1) #first checks the instance in class B then checks in the class from which it inherites from
# If there was no instance variable in class A then it prints the variable it finds in class B or class A if it doesn't find the variable in B
# print(b.special) throws error because the constuctor has been overwritten as self.special is not there in class B
#print(b.special,b.var1,b.classvar1) #when super is called just after init
print(b.special,b.var1,b.classvar1) #when super is called after the instance variable
