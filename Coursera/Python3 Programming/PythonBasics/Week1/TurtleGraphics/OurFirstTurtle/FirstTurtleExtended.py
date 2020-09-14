import turtle

color = input("Enter the background color: ")

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color(color)
alex.forward(150)
alex.left(90)
alex.forward(75)

alex.chappal = 50000
print(alex.chappal)


wn.exitonclick()

