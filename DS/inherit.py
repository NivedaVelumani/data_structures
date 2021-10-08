class Vehicle:
    def __init__(self, mil , speed):
        self.mil = mil
        self.speed=speed

    def show_details(self):
        print("I am a Bosh")
        print("mileage of the bosh:",self.mil)
        print("speed of the bosh:",self.speed)

class Car(Vehicle):
    def __init__(self, mil , speed ,cost , hp):
        super().__init__(mil, speed)
        self.cost = cost
        self.hp=hp

    def show_car_details(self):
        print("cost of the car",self.cost)
        print("hp of the car",self.hp)
        
c1=Car(2000,245,'four',260)
c1.show_details()
c1.show_car_details()

