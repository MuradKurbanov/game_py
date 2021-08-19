import pygame
import sys


def events(gun):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.m_right = True
            elif event.key == pygame.K_a:
                gun.m_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.m_right = False
            elif event.key == pygame.K_a:
                gun.m_left = False