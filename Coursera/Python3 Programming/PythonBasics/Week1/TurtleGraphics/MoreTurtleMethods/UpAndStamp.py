import turtle

wm = turtle.Screen()
wm.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

dist = 5
tess.up()  # as tess moves it doesn't leave a line

for _ in range(30):
    tess.stamp()  # stamps tess' current location
    tess.forward(dist)
    tess.right(24)
    dist += 2

wm.exitonclick()

