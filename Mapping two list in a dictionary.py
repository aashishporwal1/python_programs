List1=['a','b','c','d','e']
List2=[1,2,3,4,5]
dict={}
for key in List1:
    for value in List2:
        dict[key]=value
        List2.remove(value)
        break
print(dict)
