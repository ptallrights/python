#!/usr/bin/env python
# coding:utf-8
# __author__ = 'ptallrights'

"""
@version: Python 2.7.11
@author: ptallrights
@license: Apache Licence 
@file: Pygame.py.py
@time: 2016/7/22 19:47
"""

import pygame
import sys,random
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
#pygame.draw.circle(screen,[255,0,0],[320,240],30,0)
#my_list = [250,150,300,200]
#pygame.draw.rect(screen,[255,0,0],my_list,0)
#my_rect = pygame.Rect(250,150,300,200)
#pygame.draw.rect(screen,[255,255,0],my_rect,2)
#for i in range(100):
#    width = random.randint(0,250)
#    height = random.randint(0,100)
#    top = random.randint(0,400)
#    left = random.randint(0,500)
#    pygame.draw.rect(screen,[0,0,0],[left,top,width,height],1)
for i in range(100):
    width = random.randint(0,250)
    height = random.randint(0,100)
    top = random.randint(0,400)
    left = random.randint(0,500)
    color_name = random.choice(THECOLORS.keys())
    color = THECOLORS[color_name]
    line_width = random.randint(1,3)
    pygame.draw.rect(screen,[0,0,0],[left,top,width,height],1)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()