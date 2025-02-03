
#  Introduction

#import a function
import functions

print("Hello, I am vasiuddin mohammed")

'''
this is multi line comments
'''

#variable
a = 112
b = "apple"

print(a,b)

# Varible
c = 1232
d = 0.1235
e = False

#type of variable
print(type(c),type(d),type(e))

print(True == 1)
print(False == 0)

# Conditional Operators
age = 25
if age>18:
 print("you are voter")
elif age<18:
    print("await")

# Looging Statements
g = [1,2,3,4,5,6,7,8,9,10]

for i in g:
    print(i+1)

for j in range(90,100,2):
   print(j)

h = "india"

for k in h:
   print(k)

i = 100
while i<110:
   print(i)   
   i += 1

for i in range(1,10):
    for j in range(1,10):
      print(i+j)

j = "OsmaniaUnversity"

#break
for i in j:
   if i=="U":
    break
   print(i)

   
#continue
for i in j:
   if i=="U":
    continue
   print(i)

functions.add(2,6)
functions.sub(78,36)