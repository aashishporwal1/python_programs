def palindromeString():

    str=input("Enter the string  :")
    reverse=str[::-1]
    if str==reverse:
        print(str,"is palindrome")
    else:
        print(str,"is not palindrome")

palindromeString()
