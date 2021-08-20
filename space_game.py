import pygame
import controller
from gun import Gun
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('py_game')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()

    while True:
        controller.events(screen, gun, bullets)
        gun.update_gun()
        controller.update(bg_color, screen, gun, bullets)
        controller.update_bullets(bullets)


run()
