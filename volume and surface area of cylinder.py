pi=22/7
r=int(input("Enter the radius in cm:"))
h=int(input("Enter the height in cm:"))

Volume=pi*r*r*h
Surface_area= 2*pi*r*h + 2*pi*r*r
print("Volume of cylinder is :",round(Volume,2))
print("Surface area of cylinder is :",round(Surface_area,2))
