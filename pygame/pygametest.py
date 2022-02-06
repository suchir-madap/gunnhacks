import pygame
import time
from pygame.locals import *

pygame.init()

board_height, board_width = 500, 500
board = pygame.display.set_mode((board_height, board_width))

pygame.display.set_caption("BOARD DISPLAY")
board.fill((100, 20, 5))
pygame.display.flip()

block = pygame.image.load("head_right.png")
blockX, blockY = 50, 75
rect = block.get_rect
#rect.center = 250, 25

def img_display(board_height, board_width):
    board.blit(block, (board_height, board_width))


running = True

while running:

    #pygame.draw.rect(board, color, head, 200)
    img_display(board_height, board_width)
    board.blit(block, (250, 250))
    pygame.display.update

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_DOWN:
                board.fill((100, 100, 100))
                pygame.display.flip
        elif event.type == QUIT:
            running = False

print("done")