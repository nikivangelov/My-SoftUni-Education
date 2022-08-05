class Vehicle:

    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, owner_price, new_owner):
        if owner_price >= self.price:
            if self.owner is None:
                self.owner = new_owner
                return f"Successfully bought a {self.type}. Change: {owner_price - self.price}"
            else:
                return "Car already sold"
        else:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.sell()
print(vehicle)
print(vehicle.sell())
print(vehicle)
print(vehicle.buy(40000, "Peter"))

print(vehicle.buy(10000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
