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
        self.grid = [[0 for col in range(10)] for row in range(23)]
        self.dropShape()
    
    def update(self, screen):
        for shape in self.shapes:
            shape.update(screen)
        if len(self.shapes) > 0 and not self.shapes[-1].falling:
            self.activeShape = -1
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x-3, self.y-3, self.width+3, self.height+3), 2)
    
    def moveShape(self, direction):
        if self.activeShape != -1:
            self.activeShape.move(direction)

    def onShapeLand(self, shape):
        self.activeShape = -1
        self.dropShape()

    def fall(self):
        if self.activeShape != -1:
            self.activeShape.fall()

    def dropShape(self):
        self.activeShape = self.getRandomShape()
        self.shapes.append(self.activeShape)
        for y in range(3):
            for x in range(len(self.activeShape.grid[y])):
                if self.activeShape.grid[y][x] == 1:
                    self.grid[y][3+x] = 9
                    self.activeShape.positions.append((y, 3+x))
    
    def getRandomShape(self):
        num = random.randint(0, 6)
        x = self.x+3*Shape.SQUARE
        y = self.y-Shape.SQUARE*3
        match num:
            case 0:
                return Line(self)
            case 1:
                return Square(self)
            case 2:
                return L(self)
            case 3:
                return L2(self)
            case 4:
                return Zig(self)
            case 5:
                return Zig2(self)
            case 6:
                return T(self)
    
    def print(self):
        print('----------')
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                print(self.grid[y][x], end='')
            print('\n')
        print('----------')
