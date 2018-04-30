import pygame, sys
from pygame.locals import *
import random
import os

HEIGHT = 600
WIDTH = 800
FPS = 24
GRAV = -9.8

red = [255, 0, 0]

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Requis' adventure")
pygame.display.set_icon(pygame.image.load('idle (1).png'))
clock = pygame.time.Clock()
param = '1'
playerIdle = ('Z:/EdgyNigerianScammers/Ninga/Idle/idle (1).png')

imageListPlayer1 = []
imageListPlayer1.append(pygame.image.load('Z:/EdgyNigerianScammers/Ninga/Idle/idle (1).png'))
imageListPlayer1.append(pygame.image.load('Z:/EdgyNigerianScammers/Ninga/Idle/idle (2).png'))
imageListPlayer1.append(pygame.image.load('Z:/EdgyNigerianScammers/Ninga/Idle/idle (3).png'))
imageListPlayer1.append(pygame.image.load('Z:/EdgyNigerianScammers/Ninga/Idle/idle (4).png'))
imageListPlayer1.append(pygame.image.load('Z:/EdgyNigerianScammers/Ninga/Idle/idle (5).png'))
imageListPlayer1.append(pygame.image.load('Z:/EdgyNigerianScammers/Ninga/Idle/idle (6).png'))
imageListPlayer1.append(pygame.image.load('Z:/EdgyNigerianScammers/Ninga/Idle/idle (7).png'))
imageListPlayer1.append(pygame.image.load('Z:/EdgyNigerianScammers/Ninga/Idle/idle (8).png'))
imageListPlayer1.append(pygame.image.load('Z:/EdgyNigerianScammers/Ninga/Idle/idle (9).png'))
imageListPlayer1.append(pygame.image.load('Z:/EdgyNigerianScammers/Ninga/Idle/idle (10).png'))

imageListPlayer2 = []
imageListPlayer2.append(pygame.image.load('Z:/EdgyNigerianScammers/AnimationSheet/walk-1/walk (1).png'))
imageListPlayer2.append(pygame.image.load('Z:/EdgyNigerianScammers/AnimationSheet/walk-1/walk (2).png'))
imageListPlayer2.append(pygame.image.load('Z:/EdgyNigerianScammers/AnimationSheet/walk-1/walk (3).png'))
imageListPlayer2.append(pygame.image.load('Z:/EdgyNigerianScammers/AnimationSheet/walk-1/walk (4).png'))
imageListPlayer2.append(pygame.image.load('Z:/EdgyNigerianScammers/AnimationSheet/walk-1/walk (5).png'))
imageListPlayer2.append(pygame.image.load('Z:/EdgyNigerianScammers/AnimationSheet/walk-1/walk (6).png'))
imageListPlayer2.append(pygame.image.load('Z:/EdgyNigerianScammers/AnimationSheet/walk-1/walk (7).png'))
imageListPlayer2.append(pygame.image.load('Z:/EdgyNigerianScammers/AnimationSheet/walk-1/walk (8).png'))
imageListPlayer2.append(pygame.image.load('Z:/EdgyNigerianScammers/AnimationSheet/walk-1/walk (9).png'))



punchNinja = pygame.image.load('Z:/EdgyNigerianScammers/Ninga/punch/punch (4).png')
player = pygame.image.load(playerIdle)
player2 = pygame.image.load('player.png')

FONT = pygame.font.Font('font.ttf', 18)
GREEN = (0, 255, 0)

print(imageListPlayer1)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.param = 1
        pygame.sprite.Sprite.__init__(self)
        self.image = imageListPlayer1[self.param]
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.animTimer = 0
        self.animatedList = imageListPlayer1
        self.param2 = 1

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a] and not keystate[pygame.K_d]:
            self.speedx = -2.5
            self.image = imageListPlayer2[self.param2]
        else:
            self.image = imageListPlayer1[self.param]

        if keystate[pygame.K_d] and not keystate[pygame.K_a]:
            self.speedx = 2.5
            self.image = imageListPlayer2[self.param2]
        else:
            self.image = imageListPlayer1[self.param]
        if keystate[pygame.K_e]:
            self.image = punchNinja

        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        self.animTimer += 1
        print(self.animTimer)
        print("Param:", self.param)

        if self.animTimer >= 5:
            self.animTimer = 0
            self.param += 1
            self.param2 += 1
        if self.param >= len(self.animatedList):
            self.param = 1
        if self.param2 >= 7:
            self.param2 = 1

background = pygame.image.load('Z:/EdgyNigerianScammers/backgrounds/1.png').convert()


class Player2(Player):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player2
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 3
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -2.5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 2.5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0



enemy_sprites = pygame.sprite.Group()
enemy = Player2()
background_sprite = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
enemy_sprites.add(enemy)

screen.fill(GREEN)

running = True
while running:


    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    player.update()
    player.animTimer += 1
    enemy.update()
    enemy_sprites.update()
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    enemy_sprites.draw(screen)




    pygame.display.flip()
pygame.quit()