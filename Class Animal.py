from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk ")
class Dinosaur(Animal):
    def move(self):
        print("I Roar and run")
class Rabbit(Animal):
    def move(self):
        print("I can hop ") 
class Dog(Animal):
    def move(self):
        print("I can bark and run")
class Snake(Animal):
    def move(self):
        print("I can crawl and slither")
h = Human()
h.move()
d = Dinosaur()
d.move()
r = Rabbit()
r.move()
o = Dog()
o.move()
s = Snake()
s.move()                                           