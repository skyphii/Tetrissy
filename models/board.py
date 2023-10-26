import pygame
from models.gameobject import GameObject
from models.shape import Shape, Line, Square, L, L2, Zig, Zig2, T
import random

class Board(GameObject):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shapes = []
        self.activeShape = -1
        self.grid = [[0 for col in range(10)] for row in range(20)]
    
    def update(self, screen):
        for shape in self.shapes:
            shape.update(screen)
        if len(self.shapes) > 0 and not self.shapes[-1].falling:
            self.activeShape = -1
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x-3, self.y-3, self.width+3, self.height+3), 2)
    
    def fall(self):
        if self.activeShape != -1:
            self.activeShape.fall()

    def dropShape(self):
        self.activeShape = self.getRandomShape()
        self.shapes.append(self.activeShape)
    
    def getRandomShape(self):
        num = random.randint(0, 6)
        x = self.x+3*Shape.SQUARE
        y = self.y-Shape.SQUARE*3
        match num:
            case 0:
                return Line(x, y+Shape.SQUARE, self)
            case 1:
                return Square(x, y, self)
            case 2:
                return L(x, y, self)
            case 3:
                return L2(x, y, self)
            case 4:
                return Zig(x, y, self)
            case 5:
                return Zig2(x, y, self)
            case 6:
                return T(x, y, self)