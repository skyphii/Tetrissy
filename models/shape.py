import pygame

class Shape:

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    
    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.x, self.y, 50, 50))

    def update(self):
        if self.y < self.screen.get_height()-50:
            self.y += 1