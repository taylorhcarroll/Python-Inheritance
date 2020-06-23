from cyber_truck import CyberTruck
from lambo import Lambo
from jeep import Jeep
from motorcycle import Motorcycle
from tesla import Tesla

tesla = Tesla("black")
jeep = Jeep("yellow")
lambo = Lambo("white")
cybertruck = CyberTruck("silver")
motorcycle = Motorcycle("red")

tesla.drive()
tesla.turn("right")
tesla.stop()
print()
jeep.drive()
jeep.turn("left")
jeep.stop()
print()
lambo.drive()
lambo.stop()
print()
cybertruck.drive()
cybertruck.stop()
print()
