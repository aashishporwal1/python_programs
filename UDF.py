#User-Defined Functions to use them as library in another file
def maxoftwo(a,b):
    if a>b:
        print(a,"is greater")
    else:
        print(b,"is greater")

def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print(a,"is greater")
        else :
            print(c,"is greater")
    elif b>c:
        print(b,"is greater")
    else:
        print(c,"is greater")

def fibonacci(n):
    a,b=0,1
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()

def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print(n,"is not prime")
                break
        else:
            print(n,"is prime")
