class Figura:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self, a, b, c):
        V = a * b * c
        print('Объём:', V)

    def __str__(self):
        print(f'Высота: {self.a}, длина: {self.b}, ширина: {self.c}')

    def __add__(self, other):
        if isinstance(other, Figura):
            total_volume = self.volume() + other.volume()
            return total_volume
        else:
            raise TypeError("Можно складывать только объекты класса Figure")


class DepthFigure(Figura):
    def __int__(self, d):
        self.d = d

    def volume(self, a, b, c):
        first_figure = super().volume(a,b,c)
        second_figure = (self.a - self.d) * (self.b - self.d) * (self.c - self.d)
        third_figure = first_figure - second_figure
        print('Объем тела с внутренней вполостью:', third_figure)

    def __str__(self):
        print(f'Стороны тела с внутренней вполостью: a={self.a}, b={self.b}, c={self.c}, d={self.d}')
