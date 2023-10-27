import pygame
from time import sleep
import threading
from utils import Utils
from utils import Text
from utils import Button
from models.shape import Line
from models.board import Board

pygame.init()

Utils.WIDTH = 1200
Utils.HEIGHT = 1000

screen = pygame.display.set_mode([Utils.WIDTH, Utils.HEIGHT])
pygame.display.set_caption("Tetrissy (in-dev)")

lock = threading.Lock()
gameActive = False
gameObjects = []
board = Board(Utils.WIDTH/2-250, 0, 500, 1000)
threads = []

def update_board():
    global gameActive
    while gameActive:
        sleep(0.2)
        with lock:
            board.fall()

def start_game():
    global gameActive
    print("Game started.")
    gameObjects.clear()
    gameObjects.append(board)
    gameActive = True
    threads.append(threading.Thread(target=update_board))
    for thread in threads:
        thread.start()

gameObjects.append(Text(0, 20, "TETRISSY", 128, True))
gameObjects.append(Button(Utils.WIDTH/2-100, 300, 200, 120, "PLAY", start_game, {'normal': '#6464ff', 'hover': '#3333ff', 'pressed': '#aa33ff'}))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            gameActive = False
            for thread in threads:
                thread.join()

    screen.fill((10, 10, 10))

    for obj in gameObjects:
        obj.update(screen)

    pygame.display.flip()


pygame.quit()