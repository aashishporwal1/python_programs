List=["hey","paris","mom",'harry','rover',"dad"]
count=0
for i in List:
    if len(i)>2 and i[:1]==i[-1:]:
        count+=1
print(count)
