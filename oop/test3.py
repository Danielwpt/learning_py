class Functions:
    def receiveString(get_string):
        return get_string

class ChildFunction2(Functions):
    def receiveString(get_string, get_number, get_DateTime):
        return super().receiveString() + get_number + get_DateTime

class ChildFunction3(ChildFunction2):
    pass