str1=input("Enter your stirng :")
app_not=str1.find("not")
app_poor=str1.find("poor")

if app_not < app_poor and app_not>0 and app_poor>0 :
    str1=str1.replace(str1[app_not:(app_poor+4)],"good")
    print(str1)
else :
    print(str1)
