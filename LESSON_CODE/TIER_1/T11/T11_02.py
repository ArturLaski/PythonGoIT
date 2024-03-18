class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value

# Example usage
point = Point(5, 10)
print(point.x)  # Output: 5
print(point.y)  # Output: 10

# Changing coordinates using setters
point.x = 7
point.y = 15

print(point.x)  # Output: 7
print(point.y)  # Output: 15
