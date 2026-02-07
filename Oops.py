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


class A:               #multiple inheritance
    varA = "welcome to class A"
class B:
    varB = "welcome to class B"              
class C(A,B):
    varC = "welcome to class C"
car1 = C()
print(car1.varC)
print(car1.varA) 
