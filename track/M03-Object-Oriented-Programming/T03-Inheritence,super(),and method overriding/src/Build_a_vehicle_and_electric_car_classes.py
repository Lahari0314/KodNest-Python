class Vehicle:
    def __init__(self,brand):
        self.brand=brand

    def get_brand(self):
        return f"Brand: {self.brand}"

class ElectricCar(Vehicle):
    def get_battery(self,battery):
        return f"Battery: {battery} kwh"

brand=input().strip()
battery=int(input())
e=ElectricCar(brand)
print(e.get_brand())
print(e.get_battery(battery))