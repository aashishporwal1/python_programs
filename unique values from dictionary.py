dict1 = {'A' : [1, 3, 5, 4],
             'B' : [4, 6, 8, 10],
             'C' : [6, 12, 4 ,8],
             'D' : [5, 7, 2]}

print("The original dictionary is : " ,dict1)
  
# Using list comprehension, values() and sorted()
res = list(sorted({i for val in dict1.values() for i in val}))
  
# print result 
print("The unique values list is : " , res) 
