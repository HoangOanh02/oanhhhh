from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class Shape:
    def __init__(self, color, x_position, y_position):
        self.color=color
        self.x_position=x_position
        self.y_position=y_position

    @abstractmethod
    def Draw(self):
        pass


class Circle(Shape):
    def __init__(self, color, x_position, y_position, radius):
        super().__init__(color, x_position, y_position)
        self.__radius = radius

    def Draw(self):
        figure,axes = plt.subplots()
        Hinh_tron=plt.Circle((self.x_position, self.y_position), self.__radius, color=self.color)
        axes.set_aspect(1)
        axes.add_artist(Hinh_tron)
        plt.show()

hinhtron=Circle('red', 0.6, 0.6, 0.2)
# hinhtron.Draw()