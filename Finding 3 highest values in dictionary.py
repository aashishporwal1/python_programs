from collections import Counter
dict={"a":5,"b":2,"c":1,"d":8,"e":4,"f":9}
k=Counter(dict)
highest=k.most_common(3)
print("Initial Dictionary :")
print(dict)
print("3 Highest values are :")
for i in highest:
    print(i[0]," :",i[1]," ")
