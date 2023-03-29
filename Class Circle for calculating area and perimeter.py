class Circle():

    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.14*self.radius**2

    def perimeter(self):
        return 2*3.14*self.radius

r=int(input("Enter the radius:"))
circ=Circle(r)
print("The Area of circle is:",circ.area(),"cm sq.")
print("The Perimeter of circle is:",circ.perimeter(),"cm")
