#Input --> "09.05.1945 06:07"
#Output --> "9 May Year 1945 06 hours 07 minutes"
date="09.05.1945 06:07"
months=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
list=date.split()
a=[]
for i in list[0].split("."):
    a.append(i)


b=[]
for i in list[1].split(":"):
    b.append(i)
 
month=months[int(a[1])-1]
print(f"{a[0]} {month} Year {a[2]} {b[0]} hours {b[1]} minutes")
