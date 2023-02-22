str="Python Programming"
uc=0
lc=0
new_string=""
for i in str:
    if i.isupper():
        uc=uc+1
        new_string += (i.lower())
    elif i.islower():
        lc=lc+1
        new_string += (i.upper())
    elif i.isspace() :
        new_string += i
print("Current string :",str)
print("Total lower case letters :",lc)
print("Total upper case letters :",uc)
print("New string :",new_string)
