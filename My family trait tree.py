class FamilyMember:
    def __init__(self,eyecolor,height):
        self.eyecolor=eyecolor
        self.height=height
    
    def show_traits(self):
            print("Eye color is",self.eyecolor)
            print("Height is",self.height)
class Kid(FamilyMember):
    def __init__(self,name,age,eyecolor,height):
        super().__init__(eyecolor,height)
        self.name=name
        self.age=age
    def show_traits(self):
         print("Name:",self.name)
         print("Age:",self.age)
         super().show_traits()
    def favourite_hobby(self,hobby):
         print(self.name,"loves",hobby) 
child = Kid("Maya",10,"Brown",160)
child.show_traits()
child.favourite_hobby("Painting")
print("Is Kid a subclass of FamilyMember?",issubclass(Kid,FamilyMember))         

         
