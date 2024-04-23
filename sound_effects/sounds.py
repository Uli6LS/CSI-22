import pygame
from pygame.locals import *
from sys import exit

pygame.mixer.init()

# Carregando os sons da biblioteca
jump_sound = pygame.mixer.Sound("jump_sound.wav")
attack_sound = pygame.mixer.Sound("attack_sound.wav")
death_sound = pygame.mixer.Sound("death_sound.wav")

def play_jump_sound():
    jump_sound.play()
    
def play_attack_sound():
    attack_sound.play()

# Defina uma função para reproduzir o som de morte
def play_death_sound():
    death_sound.play()