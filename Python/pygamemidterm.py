import pygame
from random import*

(width, height) = (640, 640)
screen = pygame.display.set_mode((width, height))
background_color = (95, 200, 95)
screen.fill(background_color)
for count in range(4096):
        random_color = (randint(0,255), randint(0,255), randint(0,255))
        random_pos = (randint(0,639), randint(0,639))
        random_size = (10, 10)
        pygame.draw.rect(screen, random_color, (random_pos, random_size))
#pygame.draw.rect(screen, (255, 0, 0), (15, 10, 10, 10), 0)
pygame.display.flip()

pygame.display.set_caption("Hi Molly and Alex!")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
