def unique(lst):
    new_list=[]
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

a=["a","b",1,"b",5]
print(unique(a))
