import pygame as pg


class Player:
    def __init__(self, width, color):
        self.width = width
        self.color = color


class Circle(Player):
    def __init__(self, width, color, radius):
        super().__init__(width, color)
        self.radius = radius

    def draw_circle(self, screen, col, row):
        pg.draw.circle(screen, self.color, (int(col * 200 + 200 / 2), int(row * 200 + 200 / 2)),
                       self.radius, self.width)


class X(Player):
    def __init__(self, width, color):
        super().__init__(width, color)

    def draw_x(self, screen, col, row):
        pg.draw.line(screen, self.color, (col * 200 + 55, row * 200 + 200 - 55),
                     (col * 200 + 200 - 55, row * 200 + 55), self.width)
        pg.draw.line(screen, self.color, (col * 200 + 55, row * 200 + 55),
                     (col * 200 + 200 - 55, row * 200 + 200 - 55), self.width)
