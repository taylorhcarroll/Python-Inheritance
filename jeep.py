from vehicle import Vehicle


class Jeep(Vehicle):
    def __init__(self, color):
        self.fuel = 0
        self.main_color = color

    def drive(self):
        print(f"The {self.main_color} Jeep goes rumble rumble!")

    def refuel(self):
        self.fuel = 100
        print("The Jeep's fuel tank is now full.")

    def turn(self, direction):
        print(f"The Jeep nearly rolls over turning to the {direction}.")

    def stop(self):
        print("The Jeep comes to a halt.")
