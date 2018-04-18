import pygame, sys
from pygame.locals import *
import random
import os

HEIGHT = 480
WIDTH = 600
FPS = 24
GRAV = -9.8

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Requis' adventure")
pygame.display.set_icon(pygame.image.load('player.png'))
clock = pygame.time.Clock()

player = pygame.image.load('player.png')
player2 = pygame.image.load('player.png')

FONT = pygame.font.Font('font.ttf', 18)
GREEN = (0, 255, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -2.5
        if keystate[pygame.K_d]:
            self.speedx = 2.5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Player2(Player):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player
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

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
enemy_sprites.add(enemy)



running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.sprite.groupcollide(enemy_sprites, all_sprites, True, True)
    all_sprites.update()
    player.update()
    #enemy.update()
    enemy_sprites.update()
    screen.fill(0)
    all_sprites.draw(screen)
    enemy_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()