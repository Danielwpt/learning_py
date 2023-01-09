class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"His name is {self.name} Age is {self.age}"

Adam = Person("Adam", 12)

print(Adam)