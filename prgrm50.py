from abc import *

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def area(self):
        l=int(input("Length: "))
        b=int(input("Breadth: "))
        print("Area:",l*b)

class Triangle(Polygon):
    def area(self):
        b=int(input("Base: "))
        h=int(input("Height: "))
        print("Area:",0.5*b*h)

Rectangle().area()
Triangle().area()
