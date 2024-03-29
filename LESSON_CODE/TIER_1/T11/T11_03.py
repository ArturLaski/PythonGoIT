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
        if (type(x) == int):
            self.__x = x
        else:
            self.__x = None
            

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int):
            self.__y = y
        else:
            self.__y = None
