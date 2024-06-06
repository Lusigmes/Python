class Motors:
    
    def __init__(self, color, n_wheel, license_plate):
        self.color = color
        self.n_wheel = n_wheel
        self.license_plate = license_plate
        print("Create class")
        
    def __del__(self):
        print("Destroy class")

    def __str__(self):
        return f"{self.__class__.__name__} : {' || '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
 
    def start_motor(self):
        print("starting")
        
 
class Motorcycle(Motors):
    pass

class Car(Motors):
    pass

class Truck(Motors):
    def __init__(self, color, n_wheel, license_plate, loaded):
        super().__init__(color, n_wheel, license_plate)
        self.loaded = loaded
        
    def has_loaded(self):
        print(f"Truck {'Is' if self.loaded else 'Is not'} loaded")
        


motorcycle = Motorcycle("red", 2, "123-abc")
print(motorcycle)

car = Motorcycle("black", 4, "456-def")
print(car)

truck = Truck("white/black", 8, "789-ghi", False)
print(truck)

truck.has_loaded()