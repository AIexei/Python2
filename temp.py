import types

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def __getattribute__(self, attr_name):
        if type(object.__getattribute__(self, attr_name)) is types.MethodType:
            print(attr_name)
        return object.__getattribute__(self, attr_name)

x = Person("Lexa", 18)
print(x.get_age())
print(x.get_name())