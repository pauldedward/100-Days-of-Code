
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def change_name(self, new_name):
        self.name = new_name


user = User("edward", 28432)

print(user.id, user.name)

user.change_name("Paul")

print(user.id, user.name)
