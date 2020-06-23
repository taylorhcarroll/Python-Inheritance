class Vehicle:
    def __init__(self):
        self.main_color = ""
        self.maximum_occupancy = ""

    def drive(self):
        print("Vroooom!")

    def turn(self, direction):
        print(f"The vehicle turns to the {direction}.")

    def stop(self):
        print("The vehicle comes to a stop.")
