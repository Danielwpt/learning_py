class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Adam = Person("Adam", 12)

print(Adam.name + " " + str(Adam.age))