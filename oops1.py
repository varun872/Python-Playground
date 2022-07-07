# Classes - Template
# Object - Instance of the class
# Uses DRY "Do not Repeat Yourself"

class Student:
    pass

Varun=Student()
Raju=Student()

# print(Varun,Raju) # 2 objects at 2 different locations

Varun.name = "Varun" #creating instance of the class
Varun.std = 12
Varun.section = 'H'
print(Varun.name,Varun.std,Varun.section)
# print(Raju.name) will throw error because class Raju has no instance created

Raju.subjects=['LAA','DAA','OS','CN','MPCA']
print(Raju.subjects)
