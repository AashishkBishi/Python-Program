class parent():        #Single-level Inheritance
    a=10
    b=20
class child(parent):
    c=30
    a=40
obj=child()
print(obj.a)


class A:           #Multi-level Inheritance
    v1 = 4
    v2 = 8
class B(A):
    v3 = 8
    v4 = 16
class C(B):
    v3 = 0
    v1 = 6
obj = C()
print(obj.v1)
print(obj.v2) 


class A:               #Multiple inheritance
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"              
class C(A,B):
    varC = "welcome to class C"
car1 = C()
print(car1.varC)
print(car1.varA) 


class Parent:          #Hierarchical inheritance
    b = 8
    c = 9
class Child1(Parent):
    a = 5
    b = 7   
class Child2(Parent):
    pass
obj = Child1()
print(obj.b)


class A:           #Hybrid inheritance
    pass
class B(A):
    pass
class C(B):
    pass
class D(C, B):
    pass
print(D.mro())

output:[<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
Mro stand as Method resolving order. This method gives the order of execution of class and methods in the form of list.
