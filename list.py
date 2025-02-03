#List[]
#mutable data type
#store different type of elements
#allow duplicates
#allow indexing
#indexing: [start:stop:skip]
#positive index starts with 0 and ends with n-1
#negative index starts with -1 and end with -n

values = [1,2,3,4,5,6,7,8,9,10,"apple", "ball", "cat"]

print(values)
print(values[2])
print(values[-1])
print(values[0:2])
print(values[0:6:2])

#append
values.append("dog")
print(values)

#extend
values.extend([11,12,13,14,15,"natural"])
print(values)

#remove
values.remove("natural")
print(values)

#pop
values.pop(18)
print(values)

#index
print(values.index(12))

newValues = [10,20,30,40,50,60,70,80,90,100]

#min
print(min(newValues))

#max
print(max(newValues))

#sum
print(sum(newValues))
print(sum(newValues[0:2]))

#length
print(len(values))