import graphics
import math

n = int(input("Enter the number of sides: "))
radius = float(input("Enter the radius: "))

win = graphics.GraphWin("Regular Polygon", 500, 500)

center_x = 250
center_y = 250

angle = 360 / n

vertices = []

for i in range(n):
    theta = math.radians(i * angle)

    x = center_x + radius * math.cos(theta)
    y = center_y + radius * math.sin(theta)

    vertices.append(graphics.Point(x, y))

polygon = graphics.Polygon(vertices)
polygon.draw(win)

win.getMouse()

win.close()
