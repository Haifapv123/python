from graphics.rect import*
l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
print("rectangle Area:",area(l,b))
print("rectangle perimeter:",perimeter(l,b))

from graphics.circle import*
r=int(input("Enter radius:"))
print("circle Area:",area(r))
print("circle perimeter:",perimeter(r))

from graphics.threeD.cuboid import*
l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
h=int(input("Enter height:"))
print("cuboid Area:",area(l))
print("cuboid perimeter:",perimeter(l,b,h))

from graphics.threeD.sphere import*
r=int(input("Enter radius:"))
print("sphere Area:",area(r))
print("sphere perimeter:",perimeter(r))


