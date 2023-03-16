from collections import Counter , defaultdict
str="Aashish"
dict={}
for i in str:
    dict[i]=dict.get(i,0)+1
print(dict)
