class Parrot:
    species = "Bird"
    print("The type of species is",species)

    def __init__(self,name,age):
        self.name = name
        self.age = age 
bird = Parrot("parrot",3)

print("The bird name is",bird.name)
print("The age of the bird is",bird.age)

    