#Animal class or Parent class
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale!")


# Child class inherits from the Animal class
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water")

# Creating the fish object
golden_fish = Fish()
golden_fish.swim()
golden_fish.breathe()
print(golden_fish.num_eyes)