# Public Protected Private
class Employee:

    no_of_leaves=9 #Public-Can be accessed everywhere
    _sickdays=7 #Protected-Can be used within the class and classes derived from this class
    __emergency=14 #Private-Can be used only within this class

    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role


harry=Employee('Harry',1200000,'Data-Analyst')
print(harry.no_of_leaves)
print(harry._sickdays)

try:
    print(harry.__emergency) #will throw error because python uses something called

except Exception as e:
    print(e)

print(harry._Employee__emergency) #While calling private variables always use the class name
