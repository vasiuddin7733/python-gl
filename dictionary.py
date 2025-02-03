#Dictionary{}
#store as key-value data
#key should be immutable
#values should mutable and different data types or same
#key will act as index for element
#no slicing
#keys must unique


phones= {
   "iphone":"iphone1",
   "nokia":"nokia120"
}

#get method
print(phones.get("nokia"))

#items
print(phones.items())

#keys
print(phones.keys())

#values
print(phones.values())

#update
phones.update({"motorola":"egde 30"})
print(phones)

for i in phones.keys():
    print(i)

for i in phones.values():
    print(i)

for i,j in phones.items():
    print(i,j)


