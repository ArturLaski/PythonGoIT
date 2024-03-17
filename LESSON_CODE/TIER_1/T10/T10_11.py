class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

class Cat(Animal):
    def say(self):
        return "Meow"

class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def change_weight(self, weight):
        self.weight = weight
        
    def say(self):
        return "Meow"

# Example usage:
cat = Cat("Kitty", 5)
cat_dog = CatDog("Chupakabra", 10)

print(cat.say())       # Output: Meow
print(cat_dog.say())   # Output: Meow


    