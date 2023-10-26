import pygame
from models.gameobject import GameObject
from models.shape import Shape
from models.shape import Line
from models.shape import Square

class Board(GameObject):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shapes = []
        self.dropShape(2)
    
    def update(self, screen):
        for shape in self.shapes:
            shape.update(screen)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x-3, self.y-3, self.width+3, self.height+3), 2)
    
    def dropShape(self, column):
        # self.shapes.append(Line(self.x+column*Shape.SQUARE, -200))
        self.shapes.append(Square(self.x+column*Shape.SQUARE, -50))