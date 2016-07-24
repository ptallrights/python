#!/usr/bin/env python
# coding:utf-8
# __author__ = 'ptallrights'

"""
@version: Python 2.7.11
@author: ptallrights
@license: Apache Licence 
@file: sin.py.py
@time: 2016/7/23 17:49
"""

import pygame,sys
import math
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
plotPoints = []
for x in range(0,640):
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
    plotPoints.append([x,y])
pygame.draw.lines(screen,[0,0,0],False,plotPoints,2)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
