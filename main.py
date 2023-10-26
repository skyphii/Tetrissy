import pygame
from utils import Button
from utils import Text

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Tetrissy (in-dev)")

gameObjects = []

def test_function():
    print("working")

gameObjects.append(Text(0, 20, "TETRISSY", 128, True))
gameObjects.append(Button(WIDTH/2-100, 300, 200, 120, "PLAY", test_function, {'normal': '#6464ff', 'hover': '#3333ff', 'pressed': '#aa33ff'}))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((10, 10, 10))

    for obj in gameObjects:
        obj.update(screen)

    pygame.display.flip()


pygame.quit()