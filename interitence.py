'''
single inheritence
multilevel inheritence
multiple inheritence
hierarchical inheritence

'''

#single inheritence
class parent():
    def outputp(self):
        print("this is a parent class")

class child(parent):
    def outputc(self):
        print(" this is a child class")

child1 = child()
child1.outputc()
child1.outputp()

#multilevel intheritence
class grandparent():
    def outputgp(self):
        print("this is a grand-parent class")

class parent(grandparent):
    def outputp(self):
        print("this is a parent class")

class child(parent):
    def outputc(self):
        print(" this is a child class")

child2 = child()
child2.outputc()
child2.outputp()
child2.outputgp()

#multiple inheritence
class father():
    def outputf(self):
        print("this is a father class")

class mother():
    def outputm(self):
        print("this is a mother class")

class child(father,mother):
    def outputc(self):
        print(" this is a child class")

child3 = child()
child3.outputc()
child3.outputf()
child3.outputm()

#hierarchical inherience

class father():
    def outputf(self):
        print("this is a father class")

class child1(father):
    def outputc1(self):
        print("this is a child1 class")

class child2(father):
    def outputc2(self):
        print(" this is a child2 class")

child4 = child1()
child5 = child2()
child4.outputc1()
child4.outputf()
child5.outputc2()
child5.outputf()
