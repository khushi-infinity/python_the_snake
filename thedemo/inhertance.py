#Animal class or Parent class
class Animal:
    def __init__(self):
        print("Animal")


# Child class inherits from the Animal class
class Fish(Animal):
    def __init__(self):
        super().__init__()
        print("Fish")

# Creating the fish object
golden_fish = Fish()