#1) a. Duck typing as explained in the video is another way 
#      to achieve polymorphism besides inheritance. It states that the object
#     the object must have the minimum necessary attributes or methods.

#  b. The car having the method speak so that it has the minimum necessary
#     methods to consider it as an animal even though it did not inherit from the
#     animal class.

#2)

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on the water.")

class Drone:
    def move(self):
        print("The drone flies in the air.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)