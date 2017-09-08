"""
Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.
Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.
"""

dic = {'name':'zara','age':7,'class':'first'}
print(dic['name'])
print(dic['age'])

#update existing entry
dic['age'] = 20
#add new antry
dic['school'] = 'DPS school'

print(dic)

dic.clear()
del  dic
print(dic)