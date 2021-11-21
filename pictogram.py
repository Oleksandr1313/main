from turtle import *
import random

colors = ['red', 'white', 'yellow', 'blue', 'green', 'purple', '#ff69b4', 'cyan', 'magenta', '#faebd7', '#2e8b57', '#eeefff', '#da70d6', '#ff7f50', '#cd853f', '#bc8f8f', '#5f9ea0', '#daa520']
random.shuffle(colors)

def pictogram(colors):
    bgcolor('black')
    pensize(3)
    speed(0)

    for i in range(2):
        for colours in colors:
            color(colours)
            left(35)
            for i in range(3):
                forward(200)
                left(120)

    exitonclick()

pictogram(colors)