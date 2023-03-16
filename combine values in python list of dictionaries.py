from collections import Counter
List=[{"item":"item1","amount":400},{"item":"item2","amount":300},
      {"item":"item1","amount":750}]
result=Counter()

for i in List:
    result[i["item"]] += i["amount"]
print(result)
