class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunct(self):
        print("My name is:" + self.name)

x=Person("Kanchan",23)
x.myfunct()
print(x.name)
print(x.age)