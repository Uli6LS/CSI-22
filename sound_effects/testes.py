import pygame

from pygame.locals import *
from sys import exit

pygame.init()

LARGURA = 800
ALTURA = 640

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo CSI-22')

while True:
    for event in pygame.eve.t.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    pygame.draw.rect(tela, (200, 0, 200), (200, 300, 40, 50))
    
    pygame.display.update()
    
    