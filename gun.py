import pygame


class Gun:

    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load('images/pixel_gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.m_right = False
        self.m_left = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        if self.m_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1

        if self.m_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 1
