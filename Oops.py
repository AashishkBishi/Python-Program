class parent():        #Single-level Inheritance
    a=10
    b=20
class child(parent):
    c=30
    a=40
obj=child()
print(obj.a)
