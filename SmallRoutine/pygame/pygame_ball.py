#!/usr/bin/env python
# coding:utf-8
# __author__ = 'ptallrights'

"""
@version: Python 2.7.11
@author: ptallrights
@license: Apache Licence 
@file: picture.py.py
@time: 2016/7/23 20:16
"""
"""
import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_cat = pygame.image.load("beach_ball.png")
screen.blit(my_cat,[50,50])
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
"""

import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")
x = 50
y =50
screen.blit(my_ball,[x,y])
pygame.display.flip()
for looper in range(1,100):
    pygame.time.delay(20)
    pygame.draw.rect(screen,[255,255,255],[50,50,90,90],0)
    x = x + 5
    screen.blit(my_ball,[x,y])
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
