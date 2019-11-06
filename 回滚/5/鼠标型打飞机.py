import pygame
import random
from Vec2d import Vec2d
import copy
# 导入素材文件
background = './bg.png'
my_plan_picture = './plane01.png'
enemy_picture = './enemy.png'
my_bullet_picture = './bullet.png'
enemy_bullet_picture = './emenybullet.png'
pygame.init()
FPS = 120
fc_lock = pygame.time.Clock()


class Plan(object):
    def __init__(self):
        # 设置屏幕
        self.screen = pygame.display.set_mode((480, 800))
        # 加载素材图片
        self.background = pygame.image.load(background).convert()
        self.my_plan_picture = pygame.image.load(my_plan_picture).convert_alpha()
        self.enemy_picture = pygame.image.load(enemy_picture).convert_alpha()
        self.my_bullet_picture = pygame.image.load(my_bullet_picture).convert_alpha()
        self.enemy_bullet_picture = pygame.image.load(enemy_bullet_picture).convert_alpha()
        # 时间标志
        # self.clock = pygame.time.Clock()
        self.time_record = 0
        # 存在的各种子弹数组
        self.my_bullets = []
        self.enemy_bullets = []
        # 本机子弹速度和数量
        self.my_bullet_speed = 20
        self.my_bullet_number = 1
        # 存在的敌机
        self.live_enemy = []
        # 正在爆炸的坐标
        self.booming_pos = []
        # 初始化本机
        # 位置
        self.my_plan_pos = [288, 703]
        self.now_plan_picture = self.my_plan_picture
        # 初始化敌机
        # 位置
        self.enemy_pos = [0, 0]
        self.now_enemy_picture = self.enemy_picture
        self.enemy_dic = 4

    def move_my_plan(self):
        # 获得鼠标偏移量, 赋值给my_plan_move
        my_plan_move = pygame.mouse.get_rel()
        # 超出边界则不移动
        if 0 < self.my_plan_pos[0] + self.my_plan_picture.get_width() / 2 + my_plan_move[0] < 480:
            # 如果飞机的的x坐标的中点+偏移量在(0, 480)内
            self.my_plan_pos[0] += my_plan_move[0]
            # 飞机移动
        if 0 < self.my_plan_pos[1] + self.my_plan_picture.get_height() / 2 + my_plan_move[1] < 800:
            # 如果飞机的的y坐标的中点+偏移量在(0, 800)内
            self.my_plan_pos[1] += my_plan_move[1]
        # 把飞机显示在屏幕上
        self.screen.blit(self.now_plan_picture, self.my_plan_pos)

        # 创造本机子弹

    def create_my_bullet(self):
        # 间隔某段时间就添加子弹
        if self.time_record % self.my_bullet_speed == 0:
            if self.my_bullet_number == 1:
                self.my_bullets.append([self.my_plan_pos[0] + 40, self.my_plan_pos[1] - 13])
            elif self.my_bullet_number == 2:
                self.my_bullets.append([self.my_plan_pos[0] + 53, self.my_plan_pos[1] - 13])
                self.my_bullets.append([self.my_plan_pos[0] + 83, self.my_plan_pos[1] - 13])
        # 子弹轨迹
        for bullet in self.my_bullets:
            if bullet[1] <= 0:
                # 销毁超出范围的子弹
                self.my_bullets.remove(bullet)
            else:
                # 没超出范围则向上移动4像素
                bullet[1] -= 6
                self.screen.blit(self.my_bullet_picture, bullet)

    def create_enemy(self):
        if self.enemy_dic == 4:
            self.enemy_pos[0] += 2
            if self.enemy_pos[0] > 480-97:
                self.enemy_dic = 3
        if self.enemy_dic == 3:
            self.enemy_pos[0] -= 2
            if self.enemy_pos[0] < 0:
                self.enemy_dic = 4
        self.screen.blit(self.now_enemy_picture, self.enemy_pos)

    def judge_damage_enemy(self):
        width = self.enemy_picture.get_width()
        height = self.enemy_picture.get_height()
        for bullet_pos in self.my_bullets:
            enemy_pos = copy.deepcopy([self.enemy_pos[0], self.enemy_pos[1]])
            if enemy_pos[0] - width / 2 <= bullet_pos[0] <= enemy_pos[0] + width / 2 and enemy_pos[1] <= bullet_pos[1] <= enemy_pos[1] + height:
                # 删除击中敌机的子弹
                self.my_bullets.remove(bullet_pos)
                print("dead")

        # 开始主循环
    def began(self):
        over = 0
        while 1:
            # 隐藏鼠标
            pygame.mouse.set_visible(False)
            # 时间标志
            self.time_record += 1
            # time_pass = self.clock.tick()
            # pass_second = self.time_pass/1000.0
            # 判断退出
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    exit()
            self.move_my_plan()
            self.create_my_bullet()
            self.create_enemy()
            self.judge_damage_enemy()

                # elif event.type == pygame.KEYDOWN:
                #     keys_press = pygame.key.get_pressed()
                #     # alt+f4退出
                #     if keys_press pygame.[K_LALT] and keys_press[K_F4]:
                #         pygame.display.quit()
                #         exit()
            #         # 调节难度
            #         elif keys_press[K_LCTRL]:
            #             if self.hard != 5:
            #                 self.hard += 1
            #             else:
            #                 self.hard = 0
            #     # 使用能量
            #     elif event.type == MOUSEBUTTONDOWN and self.my_power > 0:
            #         self.sub_my_power = 1
            #     elif event.type == MOUSEBUTTONUP:
            #         self.my_bullet_speed = 20
            #         self.my_bullet_number = 1
            #         self.sub_my_power = 0
            # # 消耗能量
            # if self.sub_my_power == 1 and self.my_power > 0:
            #     self.my_bullet_speed = 10
            #     self.my_bullet_number = 2
            #     self.my_power -= 1.9
            # else:
            #     self.my_bullet_speed = 20
            #     self.my_bullet_number = 1
            # # 恢复能量
            # if self.my_power < 1000:
            #     self.my_power += 0.4
            # self.screen.blit(self.background, (0, 0))
            # self.remove_not_defeat()
            # if self.boss_life > 0:
            #     self.create_boss()
            # else:
            #     self.have_boss = 0
            # self.move_my_plan()
            # self.create_enemy()
            # self.create_my_bullet()
            # self.create_enemy_bullet()
            # self.judge_damage_enemy()
            # # 无敌状态
            # if self.is_not_defeat == 0:
            #     self.judge_damage_me()
            # self.move_box()
            # self.show_box()
            # self.boom()
            # self.draw_life_count()
            # 结束游戏
            # if self.my_life < 0:
            #     over += 1
        # if over == 1:
        #     font = pygame.font.SysFont('kaiti', 50, True)
        #     text = font.render('Game Over!', True, (255, 20, 50))
        #     self.screen.blit(text, (800, 400))
        #     # text = font.render('最终得分 %d' % self.my_count, True, (255, 20, 50))
        #     # self.screen.blit(text, (780, 500))
        #     pygame.display.update()
            # if self.my_life >= 0:
            pygame.display.update()
            self.screen.blit(self.background, (0, 0))
            fc_lock.tick(FPS)


plane = Plan()
plane.began()



