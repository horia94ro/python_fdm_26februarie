class Cat:

    age = 3
    def __init__(self, size, color, weight, name = "Leia"):
        self.size = size
        self.color = color
        self.weight = weight
        self.has_tail = True
        self.name = name

    def say_meow(self):
        print("MEOW! I am a {0} {1} cat".format(self.weight, self.color))
        self.owner = "Owen"

    def play(self, my_cat):
        print(f"I am a {self.color} cat and I am playing with a {my_cat.color} cat")

############################################################################
# print(Cat.age)
# # c1 = Cat("small", "grey", 4.5)
# # c2 = Cat("big", "white", 5.2)
# print(Cat.age) #DO IT LIKE THIS
# print(c1.age) #DON'T DO IT LIKE THIS
# print(c2.age)
# print(c1.owner)
# c1.say_meow()
# c2.say_meow()
# print(c1.owner)
# c1.play(c2)
# print(c1.size)
# print(c1.weight) # 4.5
# c1.weight = 4.7
# print(c1.weight) # 4.7
import math
class Point:




    def __init__(self, x, y):
        self._x = x
        self._y = y

    def change_x(self, new_x):
        self._x = new_x

    def change_y(self, new_y):
        self._y = new_y

    def compute_distance(self, p):
        distance = math.sqrt( (p._x - self._x) * (p._x - self._x) +
                              (p._y - self._y) * (p._y - self._y) )
        return distance


p1 = Point(0,0)
p2 = Point(1,1)
print(p1.compute_distance(p2))
# p1.change_x(10)






















