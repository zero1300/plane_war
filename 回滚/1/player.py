import pygame
from cons import *
import random


class Plane:
    def __init__(self, x, y, image=pygame.image.load(r'C:\Users\hipaa\OneDrive\Pictures\hero_plane.png')):
        self.image = image
        self.x = x
        self.y = y
        self.direction = 5

    def blit(self, screen):
        screen.blit(self.image, (self.x, self.y))
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


class Bullet:
    def __init__(self, plane, image=pygame.image.load(r'D:\Users\hipaa\Desktop\一些文件\打飞机游戏\素材\15465750502243.png')):
        self.x = plane.x + 97//2-1
        self.y = plane.y
        self.image = image

    def fly(self):
        self.y -= 35

    def blit(self, screen):
        screen.blit(self.image, (self.x, self.y))
        self.fly()
