class Bike:
    
    def __init__(self, color, model, year, price):
        print("Create class")
        self.color = color
        self.model = model
        self.year = year
        self.price = price
        self.march = 1
            
    def __del__(self):
        print("Destroy class")
            
    def beep(self):
        print("bibi")
    
    def run(self):
        print("running")
    
    def stop(self):
        print("stopping")
        print("bike stopped")  
    
    # def __str__(self):
    #     return f"Bike : {self.color} , {self.model} , {self.year}, {self.price}"
   
    def __str__(self):
        return f"{self.__class__.__name__} : {' || '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def trade_march(self, num):
        print("trading march")
        _self = self
        def _trade_march():
            if num > _self.march:
                print(f"traded march to {num}")
            else:
                print("can't trade march")
                
    def create_bike():
        bike = Bike("yellow", "Trek", 2020, 1500)
        print("Model: ", bike.model)


monarc = Bike("red","Monarc", "2000", "500")
caloi = Bike("black/white","Caloi", "2022", "2500")

print(monarc)
print(caloi)

del monarc
del caloi 

print("TEST TEST")
print("TEST TEST")

Bike.create_bike()

             
             