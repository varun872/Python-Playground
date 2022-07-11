# Class Methods as an Alternate Constuctor
class Employee:

    no_of_leaves=9

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    @classmethod
    def change_leaves(cls,newleaves): #cls here is the class(Employee)
        cls.no_of_leaves=newleaves #uses the class to change the no of leaves

    @classmethod
    def from_str(cls,string):
        # params=string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printfunc():
        return "This is a static method function"


harry=Employee('Harry',1200000,'Data-Analyst')
larry=Employee('Larry',1300000,'Data-Scientist')
varun=Employee.from_str("Varun-2000000-ML_Engineer")
print(varun.salary)
print(larry.printfunc())

# Static Methods are use to do stuff without inclusion of class methods
