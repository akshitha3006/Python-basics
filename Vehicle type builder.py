class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} vehicle is starting.")
class Car(Vehicle): 
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def start(self):
        print(f"{self.brand} {self.model} car is starting.")
my_car = Car("Toyota", "Camry")
my_car.start()
print("Is carva subclass of Vehicle?", issubclass(Car, Vehicle))     
