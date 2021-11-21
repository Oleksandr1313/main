from tutrle import *

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

pictogram()