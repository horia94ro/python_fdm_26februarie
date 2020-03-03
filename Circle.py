import math
class Circle:

    def __init__(self, r):
        self.r = r



    def __str__(self):
        return "This circle has the R = {}".format(self.r)

    def __eq__(self, other):
        if type(other) == type(self):
            if self.r == other.r:
                return True
            else:
                return False
        else:
            print("Incorrect data type")
            return False


    def compute_area(self):
        area = self.r * self.r * math.pi
        return area



c1 = Circle(5)
c2 = Circle(5)
c3 = Circle(3)
print(c1 == c2)
print(c1 == c3)
print(c1 == "123")
print(c1)
# print(c1.compute_area())
