# Multilevel Inheritance
class Dad:
    basketball=1

    @classmethod
    def change_number(cls,new):
        cls.basketball=new

class Son(Dad):
    cricket=5

    @staticmethod
    def crickter():
        return f"Yes I am a cricketer"

    def no_of_matches(self):
        return f"I have played {self.cricket} number of matches"

class Grandson(Son):
    cricket=20
    basketball=15

    @staticmethod
    def professional():
        return f"Yes I play both cricket and basketball"

    def no_of_matches(self): #Overwriting the no_of_matches function in class Son
        return f"Played {self.cricket} cricket matches and {self.basketball} basketball matches"


Thatha=Dad()
Appa=Son()
Varun=Grandson()

print(Appa.no_of_matches())
print(Varun.no_of_matches())
print(Appa.basketball) #Inherites basketball instance from Dad class because class Son inherites from class Dad
Thatha.change_number(3)
print(Thatha.basketball)
