import operator
d = {'a': 2, 'b': 4, 'c': 3, 'd': 1, 'e': 0}
print('Original dictionary : ',d)
sd = sorted(d.items(), key=operator.itemgetter(1))
print('Ascending order : ',sd)
sd = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Descending order : ',sd)
