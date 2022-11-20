import numbers
from abc import abstractmethod, ABCMeta


class Shape(metaclass=ABCMeta):

    def __int__(self, shape_type: str):
        self.__shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    __pi: numbers = 3.1416

    def __init__(self, radius: numbers):
        Shape.__init__('Circle')
        self.radius = radius

    def calculate_area(self):
        return round(Circle.__pi * (self.radius ** 2), 2)

    def calculate_perimeter(self):
        return round(2 * Circle.__pi * self.radius, 2)


class Rectangle:

    def __init__(self, length: numbers, breadth: numbers):
        Shape.__init__('Rectangle')
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.lenght + self.breadth)


circle = Circle(3)
print(f'Circle Area: {circle.calculate_area()}')
print(f'Circle Perimeter: {circle.calculate_area()}')

rectangle = Rectangle(3, 4)
print(f'Rectangle Area: {rectangle.calculate_area()}')
print(f'Rectangle Perimeter: {rectangle.calculate_area()}')


print(Shape.calculate_area('circle'))
