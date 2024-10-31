
class Vehicle:
    def __init__(self, cost, miles):
        self.miles = miles
        self.cost = cost

    def show_details(self):
        print("I am a Vehicle")
        print("mileage of Vehicle is", self.miles)
        print("cost of Vehicle is", self.cost)

    def __str__(self):
        return f"{self.cost} cost, {self.miles} miles"

class Car(Vehicle):
    pass