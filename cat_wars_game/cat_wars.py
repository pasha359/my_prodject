import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from statistics import Statistic
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Ranjer cat')
    bg_color = (0,0,0)
    gun = Gun(screen)
    bullets = Group()
    alia = Group()
    controls.create_army(screen, alia)
    stats = Statistic()
    score = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, score, gun, alia, bullets)
            controls.update_bulets(screen, stats, score, alia, bullets)
            controls.update_alias(stats, screen, score, gun, alia, bullets)

run()