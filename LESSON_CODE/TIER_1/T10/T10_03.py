class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, new_weight):
        self.weight = new_weight


animal = Animal("Simon", 10)
animal.change_weight(12)  # Change the weight from 10 to 12 units
print(f"{animal.nickname}'s weight is now {animal.weight} units.")
