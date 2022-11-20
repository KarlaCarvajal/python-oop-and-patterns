from math import pi
"""
    Python default polymorphism with len function
"""

print(f'Number of characters in string {len("Technical-solution")}')
print(f'Number of elements in array {len(["Python", "Java", "C"])}')
print(f'Number of elements in object {len({"Name": "John", "Address": "Nepal"})}')


class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        pass

    def get_fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        self.length = length
        Shape.__init__(self, "Square")

    def calculate_area(self):
        return self.length**2

    def get_fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        Shape.__init__(self, "Circle")

    def calculate_area(self):
        return pi*self.radius*2


square = Square(length=5)
circle = Circle(radius=8)
print(circle)
print(circle.get_fact())
print(square.get_fact())
print(circle.calculate_area())