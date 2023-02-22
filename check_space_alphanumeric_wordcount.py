str="Python Programming is no. 01"
sp=0
ch=0
nb=0
sc=0
wc=1
for i in str :
    if i.isspace():
        sp=sp+1
        wc=wc+1
    elif i.isalpha():
        ch=ch+1
        
    elif i.isnumeric():
        nb=nb+1
    else :
        sc=sc+1
print("Total spaces :",sp)
print("Total alphabets :",ch)
print("Total numbers :",nb)
print("Total words :",wc)
print("Total special characters :",sc)
