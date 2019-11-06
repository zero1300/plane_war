import copy
import pygame
import random
import sys
import player
from cons import *


def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HIGH])
    bg = pygame.image.load(r'C:\Users\hipaa\OneDrive\Pictures\636823110037182747.png')
    plane1 = player.Plane(480//2-100 / 2, 800-97)
    enemy1 = player.Enemy()
    planebiulist = []
    while True:
        screen.blit(bg, (0, 0))
        ran = random.randint(0, 400)
        bullet1 = player.Bullet(plane1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    plane1.direction = LEFT

                elif event.key == pygame.K_RIGHT:
                    plane1.direction = RIGHT

                elif event.key == pygame.K_UP:
                    plane1.direction = UP

                elif event.key == pygame.K_DOWN:
                    plane1.direction = DOWN

                # elif event.key == pygame.K_SPACE:
                #     onezd = player.Bullet(plane1)
                #     PlaneBiuList.append(onezd)

        # if onezd != 0:
        #     onezd.draw(screen)
        # zdlist = copy.copy(PlaneBiuList)
        # for zd in zdlist:
        #     zd.draw(screen)
        #     if zd.x < 0:
        #         PlaneBiuList.remove(zd)
        if ran < 201:
            planebiulist.append(bullet1)
        for fa in planebiulist:
            fa.draw(screen)
            if fa.x < 0:
                planebiulist.remove(fa)
        plane1.blit(screen)
        enemy1.blit(screen)
        # bullet1.blit(screen, plane1)
        pygame.display.update()
        pygame.time.delay(100)
        screen.fill([255, 255, 255])


def out_string(screen, message, color, loc, size):
    # 定义out_string函数,有四个参数
    my_font = pygame.font.SysFont("宋体", size)
    # 定义字体参数
    t = my_font.render(message, True, color)
    # 渲染字体赋值给t
    screen.blit(t, loc)
    # 输出t


if __name__ == '__main__':
    main()

