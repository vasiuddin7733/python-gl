'''
Encapsulation
wrapping of variables and methods into a single unit is called as encapsulation
public
private (__)
protected (_)
'''

class encap():
    __abc = 123
    _dfe = 456
    print(__abc)
    print(_dfe)


class encap1():
    def __init__(self,a,b):
        self.__a = a
        self._b = b

class encap2(encap1):
    def output(self):
        print(self._b)

demo1 = encap2(3,8)
demo1.output()

#polymorphism

def addition(a,b):
    print(a+b)

addition(123,458)
addition("apple", "ball")
addition([1,2,3], [4,5,6])
addition((78,58),(48,96))

#data abstraction
#hiding the information about functionality, internasl process, security information

