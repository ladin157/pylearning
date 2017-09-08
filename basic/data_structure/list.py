list1 = ['physics','chemistry',1197, 2000]
list2 = [1,2,3,4,5,6]

print(list1[0])
print(list2[1:5])
print(list2)

list2[3] = 1987
print(list2)

del list2[4]
print(list2)
print(len(list2))
print(max(list2))
list2.sort()
print(list2)