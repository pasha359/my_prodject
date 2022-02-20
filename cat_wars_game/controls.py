import time
import pygame, sys
from bulet import Bulet
from alias import Alias

def events(screen, gun, bulets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.m_right = True
            elif event.key == pygame.K_LEFT:
                gun.m_left = True
            elif event.key == pygame.K_SPACE:
                new_bulet = Bulet(screen, gun)
                bulets.add(new_bulet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.m_right = False
            elif event.key == pygame.K_LEFT:
                gun.m_left = False

def update(bg_color, screen, stats, score, gun, alias, bullets):
    screen.fill(bg_color)
    score.show_score()
    for bul in bullets.sprites():
        bul.draw_bulet()
    gun.output()
    alias.draw(screen)
    pygame.display.flip()

def update_bulets(screen, stats, score, alias, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, alias, True, True)
    if collisions:
        for alia in collisions.values():
            stats.score +=10 * len(alia)
        score.image_score()
        check_high_score(stats, score)
        score.image_life()
    if len(alias) == 0:
        bullets.empty()
        create_army(screen, alias)

def gun_kill(stats, screen, score, gun, alias, bullets):
    if stats.guns_left > 0:
        stats.guns_left -= 1
        score.image_life()
        alias.empty()
        bullets.empty()
        create_army(screen, alias)
        gun.create_gun()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()

def update_alias(stats, screen, score, gun, alias, bulets):
    alias.update()
    if pygame.sprite.spritecollideany(gun, alias):
        gun_kill(stats, screen, score, gun, alias, bulets)
    alias_check(stats, screen, score, gun, alias, bulets)

def alias_check(stats, screen, score,gun, alias, bullets):
    screen_rect = screen.get_rect()
    for alia in alias.sprites():
        if alia.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, score,gun, alias, bullets)
            break

def create_army(screen, alias):
    alia = Alias(screen)
    alia_width = alia.rect.width
    numer_alias_x = int((500 - 2 * alia_width) / alia_width)
    alia_height = alia.rect.height
    number_ali_y = int((500 - 100 - 2 * alia_height) / alia_height)

    for row_number in range (number_ali_y - 1):
        for alias_number in range(numer_alias_x):
            alia = Alias(screen)
            alia.x = alia_width + alia_width * alias_number
            alia.y = alia_height + alia_height * row_number
            alia.rect.x = alia.x
            alia.rect.y = alia.rect.height + alia_height * row_number
            alias.add(alia)

def check_high_score(stats, score):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.image_high_score()
        with open ('high_score.txt', 'w') as f:
            f.write(str(stats.high_score))