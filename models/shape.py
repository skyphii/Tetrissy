import pygame
from models.gameobject import GameObject

class Shape(GameObject):
    SQUARE = 50

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.width, self.height))

    def update(self, screen):
        if self.y < screen.get_height()-self.height:
            self.y += 1
        
        self.draw(screen)

class Line(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = Shape.SQUARE
        self.height = Shape.SQUARE*4

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.width, self.height))

class Square(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = Shape.SQUARE*2
        self.height = self.width

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.width, self.height))
