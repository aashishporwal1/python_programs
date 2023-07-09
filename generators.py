def even(n):
    for i in range(2,n):
        if i%2==0:
            yield i

for value in even(21):
    print(value)
