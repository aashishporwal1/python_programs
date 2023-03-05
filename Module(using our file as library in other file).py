import UDF

while True:

    print("*"*20)
    print("1. MaxofTwo")
    print("2. MaxofThree")
    print("3. Fibonacci")
    print("4. Prime no.")
    print("5. Exit")
    print("*"*20)

    
    choice=int(input("Enter Your Choice :"))
    print("*"*20)

    if choice==1:
        a=int(input("Enter value :"))
        b=int(input("Enter value :"))
        UDF.maxoftwo(a,b)
        print("*"*20)

    elif choice==2:
        a=int(input("Enter value :"))
        b=int(input("Enter value :"))
        c=int(input("Enter value :"))
        UDF.maxofthree(a,b,c)
        print("*"*20)

    elif choice==3:
        a=int(input("Enter value :"))
        UDF.fibonacci(a)
        print("*"*20)

    elif choice==4:
        a=int(input("Enter value :"))
        UDF.prime(a)
        print("*"*20)

    else:
        print("Thankyou for using our services ")
        print("Have a nice day!!!!")
        break



















    
