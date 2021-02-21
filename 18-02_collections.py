# mytuple = ('eggs', 'bacon', 'spam', 'tea', 'beans')
# # print(mytuple[2:4])
# #
# # print(mytuple[-4])
# mylist = list(mytuple)
# # print(mylist[-4:-2])
#
# print(mylist)
# del mylist[-4:-2]
# print(mylist)
# x = mylist.pop(1)
# print(mylist)
# print(x)

cheese = ['Cornish Yarg', 'Pke', 'Oke', 'Edam', 'Stilton']
# cheese.sort()
# print(cheese)
cheese.sort(key=len)
print(cheese)
