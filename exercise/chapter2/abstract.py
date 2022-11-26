from abc import ABC, abstractmethod

class GraphicShape:
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    def calcArea(self):
        return 3.14*(self.radius**2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side
    def calcArea(self):
        return self.side**2


g = GraphicShape()

c = Circle(10)
print('The circle area is ',c.calcArea())
s = Square(12)
print('The square area is ',s.calcArea())