from collections import UserString

class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count

# Example usage:
num_str = NumberString("Hello12345World")
print(num_str.number_count())  # Output: 5
