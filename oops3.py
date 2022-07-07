class Employee:
    no_of_leaves = 8
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}"

harry=Employee()
larry=Employee()

harry.name='Harry'
harry.salary=120000
harry.role='Program Manager'

larry.name='Larry'
larry.salary=150000
larry.role='Data Scientist'

print(harry.printdetails())

# Using Constuctors
# We can pass arguements when the class is called
class Student:
    def __init__(self,name,std,section):
        self.name=name
        self.std=std
        self.section=section

    def printdet(self):
        return f"Hi I am {self.name} and I am currently studying in class {self.std} in {self.section} section"

varun = Student('Varun',12,'A')
print(varun.printdet())
