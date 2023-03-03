num=int(input("Enter your number :"))
original=num
reverse=0
while num>0:
    tmp=num%10
    reverse=reverse*10+tmp
    num=num//10
if original==reverse:
    print("the number is palindrome")
else:
    print("the number is not palindrome")
