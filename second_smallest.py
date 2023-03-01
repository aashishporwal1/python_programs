def second_small(lst):
    smallest=lst[0]
    second_smallest=lst[0]
    for i in lst:
        if i<smallest:
            second_smallest=smallest
            smallest=i
        elif i<second_smallest and i != smallest:
            second_smallest=i
    print(second_smallest)


lst=[2,3,7,9]
second_small(lst)

