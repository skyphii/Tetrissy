import pygame
from models.gameobject import GameObject

class Button(GameObject):
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, colours={'normal': '#ffffff', 'hover': '#666666', 'pressed': '#333333'}, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.colours = colours
        self.onePress = onePress

        self.font = pygame.font.Font('font.ttf', 32)

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = self.font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

    def update(self, screen):
        mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.colours['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.colours['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.colours['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)