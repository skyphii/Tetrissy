import pygame
from models.gameobject import GameObject

class Shape(GameObject):
    SQUARE = 50

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = Shape.SQUARE*2
        self.falling = True
        self.grid = [0, 0, 0, 0],\
                    [0, 1, 1, 0],\
                    [0, 1, 1, 0],\
                    [0, 0, 0, 0]

    def draw(self, screen):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 1:
                    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x+x*Shape.SQUARE, self.y+y*Shape.SQUARE, Shape.SQUARE, Shape.SQUARE))
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x+x*Shape.SQUARE, self.y+y*Shape.SQUARE, Shape.SQUARE, Shape.SQUARE), 1)

    def update(self, screen):
        if self.y < screen.get_height()-self.height:
            self.y += 1
        else:
            self.falling = False
        
        self.draw(screen)

class Line(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.grid = [0, 0, 0, 0],\
                    [1, 1, 1, 1],\
                    [0, 0, 0, 0],\
                    [0, 0, 0, 0]

class Square(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.grid = [0, 1, 1, 0],\
                    [0, 1, 1, 0],\
                    [0, 0, 0, 0]

class L(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.grid = [1, 0, 0, 0],\
                    [1, 1, 1, 1],\
                    [0, 0, 0, 0]

class L2(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.grid = [0, 0, 0, 1],\
                    [1, 1, 1, 1],\
                    [0, 0, 0, 0]

class Zig(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.grid = [0, 1, 1],\
                    [1, 1, 0],\
                    [0, 0, 0]

class Zig2(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.grid = [1, 1, 0],\
                    [0, 1, 1],\
                    [0, 0, 0]

class T(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.grid = [0, 1, 0],\
                    [1, 1, 1],\
                    [0, 0, 0]
