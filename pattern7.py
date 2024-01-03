'''
----1
---23
--345
-4567
56789

'''
'''
for i in range(1,5+1):
    for j in range(5-i):
        print('-',end='')
    for k in range(1,i+1):
        print(k,end='')
    print()        
'''
rows = 5

for i in range(1, rows + 1):
    for j in range(rows - i):
        print("-", end="")
    for k in range(1, i + 1):
        print(k + (i - 1), end="")
    print()


