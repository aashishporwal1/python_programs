List=[1,2,3,4,5,6,7,8]
sublist=[3,4,5]
result=False

for i in range(len(List)-len(sublist)+1):
    if List[i:i+len(sublist)]==sublist:
        result=True
        break
print("Is sublist present in List :",result)
