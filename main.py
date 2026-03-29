#I call library
import pygame

print('setup start')
pygame.init()
window = pygame.display.set_mode(size=(800, 600))
print('setup end')

print('setup loopin')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
