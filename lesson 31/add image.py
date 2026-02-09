import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500,500

screen= pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_caption("Adding image and background image")


background_image = pygame.transform.scale(
    pygame.image.load("lesson 31\bg.png").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))