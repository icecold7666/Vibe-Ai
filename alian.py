import sys
import pygame
from settings import Settings
from ship import Man
import game_functions as gf
from bullet import Bullet
from pygame.sprite import Group
from army import Alien
from gamestats import Stats
from button import Button
from scoreboard import Scoreboard
def run_game():#初始化游戏并创建对象
    pygame.init()
    pygame.display.set_caption("Alien Invasion")#标题
    #设置背景颜色
    ai_settings=Settings()
    #子弹
    bullets = Group()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #创建飞船
    ship = Man(ai_settings, screen)
    #创建外星人
    # aliens = Alien(ai_settings,screen)
    aliens = Group()
    gf.create_army(ai_settings,screen,aliens,ship)

    #创建游戏统计信息
    stats = Stats(ai_settings)

    Play=Button(ai_settings,screen,"Play")

    scoreboard = Scoreboard(ai_settings, screen, stats)




    while True:#主循环

        gf.check_events(ai_settings,screen,ship, bullets, stats,Play,aliens) #响应按键和鼠标事件
        if stats.game_active:
            #运行状态
            ship.update()#更新飞船位置
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets,scoreboard,stats)#更新子弹位置
            gf.update_aliens(ai_settings,screen,ship,aliens,bullets,stats)#更新外星人位置

        gf.update_screen(ai_settings, screen, ship,aliens, bullets,Play, stats,scoreboard)#更新屏幕





#运行游戏
run_game()

