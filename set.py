'''
set{}
do not allow duplicates
no index, unorder
do not allow mutable types


set methods
add(
pop()
remove()
update()

set operators
union()
intersection
difference()
issubset()
issuperset()
'''

books = {12,24,36,48,60,72,84,96,108,120,120}

#add
books.add(132)
print(books)

#update
books.update({144,156})
print(books)

#pop
books.pop()
print(books)

#remove
books.remove(132)
print(books)

set1 = {15,30,45}
set2 = {30,45,60}

#union
print(set1.union(set2))
print(set2.union(set1))

#intersection
print(set1.intersection(set2))
print(set2.intersection(set1))

#difference
print(set1.difference(set2))
print(set2.difference(set1))

set3 = {1,2,3,4,5,6,7,8,9,10}
set4 = {1,2,3,4,5}

#issubset
print(set4.issubset(set3))

#issuperset
print(set3.issuperset(set4))


