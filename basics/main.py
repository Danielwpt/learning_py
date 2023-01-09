class Person:
    def __init__(own, name, age):
        own.name = name
        own.age = age

    def __str__(own):
        return f"His name is {own.name} Age is {own.age}"

class Police(Person):
    pass

Adam = Person("Adam", 12)

Ali = Police("Ali", 34)

print(Adam)
print(Ali.__str__())