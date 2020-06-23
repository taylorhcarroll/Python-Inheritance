from vehicle import Vehicle


class Tesla(Vehicle):
    def __init__(self, color):
        self.battery_kwh = 0
        self.main_color = color

    def drive(self):
        print(f"The {self.main_color} eletric vehicle goes zoooooooom!")

    def charge_battery(self):
        self.battery_kwh = 100
        print("The eletric vehicle's battery is now charged.")

    def turn(self, direction):
        print(f"The tesla zooms to the {direction}.")

    def stop(self):
        print("The Tesla quietly but quickly comes to a stop.")
