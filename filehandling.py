#filehandling
#reading, writing, deleting, creating of a files is called as filehandling

#modes
#read(r)
#append
#read+(r+)
#write+(w+)

'''
open
read/write
close
'''

#read(r)
file1 = open("hello.txt", mode= "r")
print(file1.read())
file1.close()


#write(w-truncate)
file2 = open("hello.txt", mode='w')
print(file2.write("hello, welcome to the python world"))
file2.close()

#append
file3 = open("hello.txt", mode='a')
file3.write(" life")
file3.close()

#read+(r+)
file4 = open("hello.txt", mode='r+')
print(file4.read())
file4.write("  rrr+")
file4.seek(0)
print(file4.read())
file4.close()


#write+(w+)
file5 = open("hello.txt", mode='w+')
file5.write(" www++")
file5.seek(0)
print(file5.read())
file5.close()


