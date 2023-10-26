import pygame
from utils import Button
from shape import Shape

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Tetrissy (in-dev)")

font = pygame.font.Font('font.ttf', 128)
title = font.render('TETRISSY', True, (0, 255, 0), (100, 100, 255))
titleRect = title.get_rect()

def test_function():
    print("working")

playButton = Button(WIDTH/2-100, 300, 200, 120, "PLAY", test_function, {'normal': '#6464ff', 'hover': '#3333ff', 'pressed': '#aa33ff'})

# shape = Shape(screen, 100, -100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((10, 10, 10))

    screen.blit(title, (WIDTH/2-titleRect.width/2, 20), titleRect)

    playButton.update(screen)

    # shape.update()
    # shape.draw()

    pygame.display.flip()


pygame.quit()