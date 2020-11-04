__author__ = "Nikolay Sergeev"

from os import system
from random import randint, choice
#while 1:
for i in range(20):
    b = randint(-1000, 1000)
    a = randint(-1000, 1000)
    system("xdotool mousemove_relative -- " + str(b) + " " + str(a))
    system("xdotool click " + str(choice([0, 1, 2, 3, 4, 5])))
