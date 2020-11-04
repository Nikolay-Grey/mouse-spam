from os import system
from random import randint
#while 1:
for i in range(20):
    b = randint(-1000, 1000)
    a = randint(-1000, 1000)
    system("xdotool mousemove_relative -- " + str(b) + " " + str(a))
    system("xdotool click 1")
