def test(a,b,c,*d,**e):
    print(" A : ",a,' B : ',b," c : ",c," D : ",d," E : ",e)

test(1,2,3,4,5,6,7,8,9,x=10,y=20,z=30)
