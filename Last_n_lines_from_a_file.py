n = int(input("Enter the number of lines :"))
filename = 'FILE.txt'

head = ''
with open(filename) as my_file:
    for x in my_file.readlines()[-n:]:
        print(x,end="")
