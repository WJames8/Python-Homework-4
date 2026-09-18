import graphics
import math

win = graphics.GraphWin("Logistic Function", 600, 500)

x_axis = graphics.Line(graphics.Point(50, 450), graphics.Point(550, 450))
y_axis = graphics.Line(graphics.Point(50, 450), graphics.Point(50, 50))

x_axis.draw(win)
y_axis.draw(win)

for x in range(100):
    y = 1 / (1 + math.exp(-x))

    screen_x = 50 + x * 5
    screen_y = 450 - y * 400

    point = graphics.Point(screen_x, screen_y)
    point.draw(win)

win.getMouse()

win.close()
