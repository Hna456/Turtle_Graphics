from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

number_of_sides = 3
colors = ["deep pink", "slate blue", "Tomato", "dark magenta", "green", "navy", "rosy brown"]

for color in colors:
    timmy.color(color)
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        timmy.right(angle)
        timmy.forward(100)
    number_of_sides += 1

screen = Screen()
screen.exitonclick()
