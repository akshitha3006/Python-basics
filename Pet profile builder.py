class Pet:
    species_type = "Domestic Animal"
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}, Species Type: {self.species_type}")
pet1 = Pet("Buddy", 3, "Golden Retriever")
pet1.display_info()
pet2 = Pet("Whiskers", 2, "Siamese Cat")
pet2.display_info()    