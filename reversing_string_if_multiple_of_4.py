str="Hello world!"
rev=""
print("Original string :",str)
if(len(str)%4==0):
    for i in str[::-1]:
        rev=rev+i
    print("Reversed string :",rev)
else :
    print("Length of string is not a multiple of 4.")
