n = int(input("Enter the number of lines :"))
filename = 'FILE.txt'

head = ''
with open(filename) as my_file:
    for x in range(n):
        head += next(my_file)
    
print(head)