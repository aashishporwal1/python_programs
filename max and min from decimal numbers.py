List=[1.2,22.45,0.1,78.8,0.001,5.98]
maximum=List[0]
minimum=List[0]
for i in List:
    if i>maximum:
        maximum=i
    elif i<minimum:
        minimum=i
print(List)
print("Maximum :",maximum)
print("Minimum :",minimum)
