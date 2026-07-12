from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon',['Pikachu','Squirtle','Charmander'])
table.add_column('Type',['Electric','Water','Fire'])
print(table)

print("----"*40)
print("----"*20 + "oops " + "----"*20)
print("----"*40)

# Object oriented programming
class CarRacer:
    pass

car_racer = CarRacer()



# calss user
class User:

#Contructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        self.following+=1
        user.followers+=1

user_1 = User("001", "Timmy")
print(user_1.id)
print(user_1.followers)

user_2 = User("002", "Johny")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)