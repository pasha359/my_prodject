import pygame

class Bulet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):

        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,3,12)
        self.color = 139,195,74
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bulet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)