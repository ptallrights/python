#!/usr/bin/env python
# coding:utf-8
# __author__ = 'ptallrights'

"""
@version: Python 2.7.11
@author: ptallrights
@license: Apache Licence 
@file: a_gui.py.py
@time: 2016/7/24 16:46
"""

import easygui
#flavor = easygui.buttonbox("What is your favorite ice cream flavor?",
#                           choices = ['Vanilla','Chocolate','Strawberry'])

#flavor = easygui.choicebox("What is your favorite ice cream flavor?",
#                           choices = ['Vanilla','Chocolate','Strawberry'])

flavor = easygui.enterbox("What is your favorite ice cream flavor?",default = "Strawberry")
easygui.msgbox ("You picked " + flavor)