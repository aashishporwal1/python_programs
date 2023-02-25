def largest_smallest_sum(lst):
    largest=lst[0]
    smallest=lst[0]
    sum=0
    for i in lst:
        sum=sum+i
        if i>largest:
            largest=i
        elif i<smallest:
            smallest=i
    print("Largest no is :",largest)
    print("Smallest no is :",smallest)
    print("Sum of all numbers is :",sum)

lst=[15,1,2,3,0,40,21,7]
largest_smallest_sum(lst)
