class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self, food_weight):
        self.weight += food_weight
        print(f"{self.name} has eaten and weighs {self.weight:} kg.")

    def sleep(self):
        print(f"{self.name} is nw sleeping.")

class Cow(Animal):
    def moo(self):
        print(f"{self.name} says 'Moo!'")

class Sheep(Animal):
    def baa(self):
        print(f"{self.name} says 'Baa!'")

class Goat(Animal):
    def mee(self):
        print(f"{self.name} says 'Mee!'")

cow = Cow(name="Burёnka", weight=150.0)
sheep = Sheep(name="Edward", weight=40.0)
goat = Goat(name="Vasya", weight=30.0)
print("-------")
cow.eat(10)
cow.moo()
cow.sleep()
print("-------")
sheep.eat(5)
sheep.baa()
sheep.sleep()
print("-------")
goat.eat(3)
goat.mee()
goat.sleep()
