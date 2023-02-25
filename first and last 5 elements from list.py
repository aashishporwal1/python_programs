lst=[]
new_list=[]
for i in range(1,31):
    lst.append(i*i)
print(lst)
new_list=lst[:5]+lst[-5:]
print(new_list)
