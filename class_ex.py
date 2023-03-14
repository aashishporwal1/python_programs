class Student:
    def getData(self,fname,lname):
        print("getData Called")
        self.f=fname
        self.l=lname
    def putData(self):
        print("putData Called")
        print("First Name :",self.f)
        print("Last Name :",self.l)

s1=Student()
s2=Student()
s1.getData("Aashish","Porwal")
s1.putData()
s2.getData("Jigar","Thakkar")
s2.putData()