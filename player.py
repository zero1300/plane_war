import pygame
from cons import *
from pygame import *


class Plane:
    def __init__(self, x, y, plane_pic=pygame.image.load(r'C:\Users\hipaa\OneDrive\Pictures\hero_plane.png')):
        self.image = plane_pic
        self.x = x
        self.y = y
        self.direction = 5
        self.plane_rect = plane_pic.get_rect()

    def blit(self, screen):
        screen.blit(self.image, self.plane_rect)
        self.move()

    def move(self):
        if self.direction == UP:
            self.y -= 15
            if self.y < 0:
                self.y = 0
        elif self.direction == DOWN:
            self.y += 15
            if self.y > 800-97:
                self.y = 800-97
        elif self.direction == LEFT:
            self.x -= 15
            if self.x < 0:
                self.x = 0
        elif self.direction == RIGHT:
            self.x += 15
            if self.x > 480-97:
                self.x = 480-97

    # def check_dead(self, enemy):
    #     if self.x == enemy.x and self.y == enemy.y:
    #         sys.exit()


# class Bullet:
#     def __init__(self, plane, screen):
#         self.x = plane.x + 97//2-1
#         self.y = plane.y
#         self.screen = screen
#         self.bullet_group = []
#         self.image = pygame.image.load(r'D:\Users\hipaa\Desktop\一些文件\打飞机游戏\素材\15465750502243.png')
#
#     def fly(self):
#         self.y -= 35
#
#     def blit(self, screen, plane):
#         self.add(plane, screen)
#         for i in self.bullet_group:
#             i.blit(plane, screen)
#         screen.blit(self.image, (self.x, self.y))
#         self.fly()
#
#     def add(self, plane, screen):
#         self.bullet_group.append(Bullet(plane, screen))
# class Bullet:
#     def __init__(self, plane, image=pygame.image.load(r'D:\Users\hipaa\Desktop\一些文件\打飞机游戏\素材\15465750502243.png')):
#         self.new_location(plane)
#         self.image = image
#
#     def blit(self, screen):
#         screen.blit(self.image, (self.x, self.y))
#         self.fly()
#
#     def fly(self):
#         self.y -= 30
#
#     def new_location(self, plane):
#         self.x = plane.x + 97//2-2
#         self.y = plane.y
class Bullet:
    def __init__(self, plane, bullet_pic=pygame.image.load(r'D:\Users\hipaa\Desktop\一些文件\打飞机游戏\素材\15465750502243.png')):
        self.x = plane.x + 97//2 - 10
        self.y = plane.y
        self.image = bullet_pic
        self.bullet_rect = bullet_pic.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.move()

    def move(self):
        self.y -= 50


class Enemy:
    def __init__(self, x=SCREEN_WIDTH/2-ENEMY_WIDTH/2, y=0, image=pygame.image.load(r'D:\Users\hipaa\Desktop\一些文件\打飞机游戏\素材\15465750502143.png')):
        self.x = x
        self.y = y
        self.image = image
        self.dic = 4
        self.live = 1
        self.shuRect = Rect(self.x + 34, self.y, 38, 81)
        self.hangRect = Rect(self.x, self.y + 18, 107, 49)

    def blit(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.move()

    def move(self):
        if self.dic == 4:
            self.x += 15
            if self.x > SCREEN_WIDTH - ENEMY_WIDTH:
                self.dic = 3
        if self.dic == 3:
            self.x -= 15
            if self.x < 0:
                self.dic = 4
