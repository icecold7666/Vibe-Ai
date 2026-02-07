import sys
from zoneinfo import available_timezones
from army import Alien
import pygame
from bullet import Bullet
from time import sleep
def check_events(ai_settings,screen,ship, bullets, stats,Play,aliens):
    """互动"""
    for event in pygame.event.get():  # 事件处理,交互
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                ship.moving_up =True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
            elif event.key == pygame.K_SPACE :
                if len(bullets) < ai_settings.bullets_allowed:
                    new_bullet = Bullet(ai_settings, screen, ship)
                    bullets.add(new_bullet)
            elif event.key == pygame.K_q:
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # check_play_button(stats,Play, mouse_x, mouse_y)
            if Play.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
                stats.game_active = True
                stats.reset_stats()
                ai_settings.initialize_dynamic_settings()
                aliens.empty()
                bullets.empty()
                create_army(ai_settings,screen,aliens,ship)
                ship.center_ship()




        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False






def update_screen(ai_settings, screen, ship,aliens, bullets,Play, stats,scoreboard):
    """更新屏幕"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # alian.blitme()
    aliens.draw(screen)
    scoreboard.show_score()
    if not stats.game_active:
        Play.draw_button()

    pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets,sb,stats):
    """更新子弹位置"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        create_army(ai_settings,screen,aliens,ship)
    if collisions:
        for alien in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_highscore(stats,sb)

def create_army(ai_settings,screen,aliens,ship):
    """创建外星人"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    available_space_x = ai_settings.screen_width - 2 * alien_width
    available_space_y = ai_settings.screen_height - 3 * alien_height- ship.rect.height
    number_aliens_x = int(available_space_x / (2 * alien_width))
    number_rows = int(available_space_y / (2 * alien_height))
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            alien = Alien(ai_settings,screen)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
            aliens.add(alien)

def change_fleet_direction(ai_settings,aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings,aliens):
    """外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break


def ship_hit(ai_settings,screen,ship,aliens,bullets,stats):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_army(ai_settings,screen,aliens,ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False

def update_aliens(ai_settings,screen,ship,aliens,bullets,stats):
    """更新外星人位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,ship,aliens,bullets,stats)
        print("Manba Out!!!")
    check_aliens_bottom(ai_settings,screen,ship,aliens,bullets,stats)

def check_aliens_bottom(ai_settings,screen,ship,aliens,bullets,stats):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,screen,ship,aliens,bullets,stats)
            break

def check_highscore(stats,sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

