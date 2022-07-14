# Multiple Inheritance
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


    def printdetails(self):
        return f"Employee is {self.name}, his salary is {self.salary} and his designation is {self.role}"

class Player:
    no_of_games = 4
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def gamedetails(self):
        return f"Player is {self.name} and he plays the following sports {self.game}"


class CoolProgrammer(Employee,Player): # Order of classes in the class is very important
    languages=['C','C++','Python','Java']
    def printlanguages(self):
        print(self.languages)


harry=Employee("Harry",450,"Manager")
varun=Player("Varun",['Cricket','Football','Basketball','TT','Badminton'])
print(varun.gamedetails())
karan=CoolProgrammer("Karan",800,"Coder")
print(karan.printdetails())
karan.printlanguages()
