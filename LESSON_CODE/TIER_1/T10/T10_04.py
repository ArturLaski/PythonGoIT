class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    @classmethod
    def change_color(cls, new_color):
        cls.color = new_color


first_animal = Animal("Simon", 10)
second_animal = Animal("Lucy", 15)

# Calling change_color method for first_animal
first_animal.change_color("red")

print(f"First animal's color: {first_animal.color}")  # Output: red
print(f"Second animal's color: {second_animal.color}")  # Output: red (changed for both instances)

        