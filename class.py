class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def bark(self):
        print(self.name + " Augwh Augwh")

firstDog = Dog("Doggy")

print(firstDog.bark())