

#functions
# block of acode
# def add (a, b):
#run when its called

def func():
    print("this is normal function")

func()

def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

add(2,3)

#function with arbitary parameters
def func1(*a):
    print("this is function with arbitary parameters", a)

func1(12,25,45)


