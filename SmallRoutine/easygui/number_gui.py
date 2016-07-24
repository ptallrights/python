#!/usr/bin/env python
# coding:utf-8
# __author__ = 'ptallrights'

"""
@version: Python 2.7.11
@author: ptallrights
@license: Apache Licence 
@file: number_gui.py.py
@time: 2016/7/24 17:16
"""

import random,easygui
secret = random.randint(1,99)
guess = 0
tries = 0
easygui.msgbox("""AHOY! I'm the Dread Pirate Roberts, and I have a secret!
It is a number from 1 to 99. I'll give you 6 tries.""")
while guess != secret and tries < 6:
    guess = easygui.integerbox("What's your guess,matey?")
    if not guess:break
    if  guess < secret:
        easygui.msgbox(str(guess) + " is too low,ye scurvy dog!")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high,landlubber!")
    tries = tries + 1
if guess == secret:
    easygui.msgbox("Avast! ye got it! Found my secret,ye did!")
else:
    easygui.msgbox("NO more guesses! The number was " + str(secret))