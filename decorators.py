def makepretty(func):
    def inner():
        print("Decorated")
        func()
    return inner

#Mention the decorator function with "@" before the normal function
@makepretty
def ordinary():
    print("Ordinary")

ordinary()
