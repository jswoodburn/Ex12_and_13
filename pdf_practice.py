a = 12
b = 15
# print(a, b)
a, b = b, a
# print(a, b)

tup = 4, 2, 5, 1
print(sorted(tup))

li = list(tup)
print(type(li),li)

print(sorted(li))

# print(li.sort()) # returns None because method sorts list internally
li.sort()
print(li)

cheese = ['cheddar', 'stilton', 'cornish yarg', 'oke', 'stilton', 'cheshire']
# cheese = list(set(cheese) - {'stilton', 'oke', 'brie'})
# print(cheese)

dairy = {'milk', 'yoghurt', 'cheddar', 'stilton'}
cheeses = set(cheese)

# print(dairy & cheeses)
# print(dairy.intersection(cheeses))

print(dairy | cheeses)

print(dairy - cheeses)
print(cheeses - dairy)

print(cheeses ^ dairy)