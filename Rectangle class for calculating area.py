class Rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width

l=int(input("Enter the Length in cm :"))
w=int(input("Enter the Width in cm :"))

rect=Rectangle(l,w)
print("The area of rectangle is",rect.area(),"cm sq.")
