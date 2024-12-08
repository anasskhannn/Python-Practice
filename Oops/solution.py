class Car:
    total_cars=0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_cars +=1
    
    def get_brand(self):
        return self.__brand +"!!!"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Current"

my_tesla=ElectricCar("Tesla", "CyberTruck", "80kWH")
print(my_tesla.model,my_tesla.fuel_type())

safari = Car("Toyota", "Supra")
print(safari.model,safari.fuel_type())

print(Car.total_cars)