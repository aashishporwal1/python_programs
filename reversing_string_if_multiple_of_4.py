str="Hello world!"
rev=""
if(len(str)%4==0):
    for i in str[::-1]:
        rev=rev+i
    print(rev)
