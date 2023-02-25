str=input("Enter you string :")
length=len(str)
if length>2 :
    if str.endswith('ing'):
        str+='ly'
    else :
        str=str+'ing'

print(str)
