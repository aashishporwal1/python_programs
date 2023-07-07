from abc import ABC
#Sides may vary in each Polygon, So we will define sides method in Derived Classes.
class Polygon(ABC):
    #abstract_method
    def sides(self):
        pass
    
class Triangle(Polygon):
    def sides(self):
        print("Triangle has 3 sides")

class Rectangle(Polygon):
    def sides(self):
        print("Rectangle has 4 sides")
        
class Square(Polygon):
    def sides(self):
        print("Square has 4 sides")
        
class Octagon(Polygon):
    def sides(self):
        print("Octagon has 8 sides")

#Creating objects of above classes
tri=Triangle()
tri.sides()

rect=Rectangle()
rect.sides()

sq=Square()
sq.sides()

oct=Octagon()
oct.sides()
