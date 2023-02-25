def same_element(lst1,lst2):
    for i in lst1:
        for j in lst2:
            if i==j:
                return True
    
a=[1,2,3,4,5,"ty"]
b=[6,7,"ty"]
print(same_element(a,b))
