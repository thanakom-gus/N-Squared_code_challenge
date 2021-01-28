
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
        


if __name__ == "__main__":
    # testing
    CircleA = Circle(3)
    print(CircleA.area(), CircleA.perimeter())


## finished time 00:06:53.23
