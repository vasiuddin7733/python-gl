
#tuple()
#immutable data type
#store different type of elements
#allow duplicates
#allow indexing and slicing
#indexing: [start:stop:skip]
#positive index starts with 0 and ends with n-1
#negative index starts with -1 and end with -n
#there is inbuilt no methods 

marks = (1,2,3,4,5)

#min
print(max(marks))

#max
print(max(marks))

#sum
print(sum(marks))
print(sum(marks[0:2]))

#length
print(len(marks))

#concatenation
t1 = (15,60,78)
t2 = (45,75,48)
t3 = t1+t2

print(t3)

#reprepetition
print(t3*2)
print(t3*3)

#membership operations
print(15 in t3)
print(15 not in t3)
print(t1 is t2)
print(t1 is not t2)