class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, (int, float)):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Vector index out of range")

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Vector index out of range")

    def __add__(self, other):
        new_x = self.coordinates.x + other.coordinates.x
        new_y = self.coordinates.y + other.coordinates.y
        return Vector(Point(new_x, new_y))

    def __sub__(self, other):
        new_x = self.coordinates.x - other.coordinates.x
        new_y = self.coordinates.y - other.coordinates.y
        return Vector(Point(new_x, new_y))

    def __call__(self, value=None):
        if value:
            self.coordinates.x *= value
            self.coordinates.y *= value
        return self.coordinates.x, self.coordinates.y

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"


# Example usage:
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 - vector1
