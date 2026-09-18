import graphics
import math

win = graphics.GraphWin("Logistic Function", 600, 500)

x_axis = graphics.Line(
    graphics.Point(50, 450),
    graphics.Point(550, 450)
)
x_axis.draw(win)

y_axis = graphics.Line(
    graphics.Point(50, 450),
    graphics.Point(50, 50)
)
y_axis.draw(win)

x = 0
y = 1 / (1 + math.exp(-x))

screen_x = 50 + x * 5
screen_y = 450 - y * 400

previous_point = graphics.Point(screen_x, screen_y)

for x in range(1, 100):
    y = 1 / (1 + math.exp(-x))

    screen_x = 50 + x * 5
    screen_y = 450 - y * 400

    current_point = graphics.Point(screen_x, screen_y)

    line = graphics.Line(previous_point, current_point)
    line.draw(win)

    previous_point = current_point

win.getMouse()

win.close()
