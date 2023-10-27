import pygame
from models.gameobject import GameObject

class Shape(GameObject):
    SQUARE = 50

    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.board = board
        self.height = Shape.SQUARE*2
        self.falling = True
        self.number = -1
        self.colour = (0, 0, 0)
        self.grid = [0, 0, 0, 0],\
                    [0, 1, 1, 0],\
                    [0, 1, 1, 0],\
                    [0, 0, 0, 0]

    def draw(self, screen):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 1:
                    pygame.draw.rect(screen, self.colour, pygame.Rect(self.x+x*Shape.SQUARE, self.y+y*Shape.SQUARE, Shape.SQUARE, Shape.SQUARE))
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x+x*Shape.SQUARE, self.y+y*Shape.SQUARE, Shape.SQUARE, Shape.SQUARE), 1)

    def update(self, screen):
        self.draw(screen)

    def fall(self):
        # self.board.print()
        if not self.isLanded():
            # print("Not Landed: " + str(self.number))
            self.y += Shape.SQUARE
            for y in reversed(range(len(self.board.grid))):
                for x in range(len(self.board.grid[y])):
                    if self.board.grid[y][x] == 9:
                        self.board.grid[y][x] = 0
                        self.board.grid[y+1][x] = 9
        else:
            # print("Landed: " + str(self.number))
            for y in reversed(range(len(self.board.grid))):
                for x in range(len(self.board.grid[y])):
                    if self.board.grid[y][x] == 9:
                        self.board.grid[y][x] = self.number
            self.falling = False
            self.board.onShapeLand(self)
    
    def isLanded(self):
        for y in range(len(self.board.grid)):
            # skip first 2 rows (above display)
            if y < 2:
                continue
            for x in range(len(self.board.grid[y])):
                if self.board.grid[y][x] == 9:
                    if y == len(self.board.grid)-1 or (self.board.grid[y+1][x] != 0 and self.board.grid[y+1][x] != 9):
                        return True
        return False

class Line(Shape):
    def __init__(self, x, y, board):
        super().__init__(x, y, board)
        self.number = 1
        self.colour = (0, 255, 255)
        self.grid = [0, 0, 0, 0],\
                    [1, 1, 1, 1],\
                    [0, 0, 0, 0],\
                    [0, 0, 0, 0]

class Square(Shape):
    def __init__(self, x, y, board):
        super().__init__(x, y, board)
        self.number = 2
        self.colour = (255, 255, 0)
        self.grid = [0, 1, 1, 0],\
                    [0, 1, 1, 0],\
                    [0, 0, 0, 0]

class L(Shape):
    def __init__(self, x, y, board):
        super().__init__(x, y, board)
        self.number = 3
        self.colour = (0, 0, 255)
        self.grid = [1, 0, 0, 0],\
                    [1, 1, 1, 1],\
                    [0, 0, 0, 0]

class L2(Shape):
    def __init__(self, x, y, board):
        super().__init__(x, y, board)
        self.number = 4
        self.colour = (255, 127, 0)
        self.grid = [0, 0, 0, 1],\
                    [1, 1, 1, 1],\
                    [0, 0, 0, 0]

class Zig(Shape):
    def __init__(self, x, y, board):
        super().__init__(x, y, board)
        self.number = 5
        self.colour = (0, 255, 0)
        self.grid = [0, 1, 1],\
                    [1, 1, 0],\
                    [0, 0, 0]

class Zig2(Shape):
    def __init__(self, x, y, board):
        super().__init__(x, y, board)
        self.number = 6
        self.colour = (255, 0, 0)
        self.grid = [1, 1, 0],\
                    [0, 1, 1],\
                    [0, 0, 0]

class T(Shape):
    def __init__(self, x, y, board):
        super().__init__(x, y, board)
        self.number = 7
        self.colour = (128, 0, 128)
        self.grid = [0, 1, 0],\
                    [1, 1, 1],\
                    [0, 0, 0]
