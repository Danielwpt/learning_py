class Users:
    def __init__(user ,Name, Age):
        user.name = Name
        user.age = Age

    def GetUserSummary(user):
        return f"{user.name} {user.age}"

class Details(Users):
    pass

    def GetUserDetail(user, Birthdate, Gender):
        return f"{user.name} {user.age} {Birthdate} {Gender}"

Dan = Details("Dan", 12).GetUserDetail("12-12-22", 'M')
print(Dan)