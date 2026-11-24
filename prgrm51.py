class Rectangle:
    def __init__(self):
        self.l=int(input("Length: "))
        self.b=int(input("Breadth: "))

    def area(self):
        return self.l*self.b

r1=Rectangle()
r2=Rectangle()

print("Area 1:",r1.area())
print("Area 2:",r2.area())

if r1.area()>r2.area():
    print("Rectangle 1 is bigger")
else:
    print("Rectangle 2 is bigger")
