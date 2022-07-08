# Class Method
class Employee:

    no_of_leaves=9

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    @classmethod
    def change_leaves(cls,newleaves): #cls here is the class(Employee)
        cls.no_of_leaves=newleaves #uses the class to change the no of leaves

harry=Employee('Harry',120000,'Data-Analyst')
larry=Employee('Larry',130000,'Data-Scientist')

print(harry.salary,larry.role)
print(harry.no_of_leaves)
harry.change_leaves(30)
print(harry.no_of_leaves)
