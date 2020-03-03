class Animal(object):

    def __init__(self, name, color):
        self.name = name
        self.color = color


    def eating(self):
        print("The animal is eating!")

    def moves(self):
        raise NotImplementedError("The moves() method is not yet implemented!")


class Bear(Animal):

    def __init__(self, name, color, hibernation_period):
        super().__init__(name, color)
        self.hibernation_period = hibernation_period

    def eating(self):
        print("The bear eats in the woods!")

    def moves(self):
        return 5.5

class Horse(Animal):

    def __init__(self, name, color, racer):
        super().__init__(name, color)
        self.racer = racer

    def races(self):
        if self.racer:
            print("My horse is racing")
        else:
            print("My horse is lazy")

    def moves(self):
        return 15

b1 = Bear("Smokey", "brown", 3.5)
h1 = Horse("McQueen", "white", True)
b1.eating() #Calling the method used for overriding in the class Bear
h1.eating() #Calling the method defined in the Animal class since Horse doesn't override it
h1.races()
print(b1.moves())
print(h1.moves())
# b1.races() #Can't do this since races() is part of the Horse class; b1 is a Bear
# print(b1.hibernation_period)
# print(b1.name)
# b1.eating()