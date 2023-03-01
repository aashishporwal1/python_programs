dict1={"a":1,"b":2,"c":3}
dict2={"e":4,"f":5}
dict3={"g":6,"h":7}
dict4={}
for i in (dict1,dict2,dict3):
    dict4.update(i)
print(dict4)
