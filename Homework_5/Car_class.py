class Car:
    def __init__(self, yearModel, make):
        self.yearModel = yearModel
        self.make = make
        self.speed = 0  

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def current_speed(self):
        return self.speed

my_car = Car(2022, "Toyota")

for i in range(5):
    my_car.accelerate()
    print(my_car.current_speed())
print("---------")
for i in range(5):
    my_car.brake()
    print(my_car.current_speed())
