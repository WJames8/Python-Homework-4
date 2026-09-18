import graphics
import math

win = graphics.GraphWin("Logistic Function", 700, 600)

points_label = graphics.Text(graphics.Point(100, 30), "Points:")
points_label.draw(win)

points_entry = graphics.Entry(graphics.Point(180, 30), 8)
points_entry.setText("100")
points_entry.draw(win)

x_axis = graphics.Line(
    graphics.Point(50, 550),
    graphics.Point(650, 550)
)
x_axis.draw(win)

y_axis = graphics.Line(
    graphics.Point(50, 150),
    graphics.Point(50, 550)
)
y_axis.draw(win)

button = graphics.Text(graphics.Point(350, 80), "Graph")
button.draw(win)

while True:
    click = win.getMouse()

    if 300 <= click.getX() <= 400 and 60 <= click.getY() <= 100:

        if button.getText() == "Exit":
            break

        number_of_points = int(points_entry.getText())

        x = 0
        y = 1 / (1 + math.exp(-x))

        screen_x = 50 + x * 6
        screen_y = 550 - y * 400

        previous_point = graphics.Point(screen_x, screen_y)

        for x in range(1, number_of_points):
            y = 1 / (1 + math.exp(-x))

            screen_x = 50 + x * 6
            screen_y = 550 - y * 400

            current_point = graphics.Point(screen_x, screen_y)

            line = graphics.Line(previous_point, current_point)
            line.draw(win)

            previous_point = current_point

        button.setText("Exit")

win.close()
