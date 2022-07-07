class Employee:
    no_of_leaves = 8
    pass

harry=Employee()
larry=Employee()

harry.name='Harry'
harry.salary=120000
harry.role='Program Manager'

larry.name='Larry'
larry.salary=150000
larry.role='Data Scientist'

print(harry.salary,larry.salary) # disjoint from each other
print(harry.no_of_leaves,larry.no_of_leaves) # common to both employees

print(harry.__dict__)
# To change the objects in Employee we have to access it thru Employee.no_of_leaves=9
# Employee.no_of_leaves = 10
harry.no_of_leaves=10
print(harry.__dict__)
print(harry.no_of_leaves,larry.no_of_leaves) # harry.no_of_leaves changes to 10 but larry.no_of_leaves will still be 8
print(Employee.no_of_leaves) 
# Doing harry.no_of_leaves=10 won't change Employee class no_of_leaves Employee.no_of_leaves will still be 8
