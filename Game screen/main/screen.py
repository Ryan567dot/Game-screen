import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Game screen")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()