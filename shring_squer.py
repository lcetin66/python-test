import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("turtle python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def shrinkingSqaure(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size -= 5

shrinkingSqaure (150)
shrinkingSqaure (130)
shrinkingSqaure (110)
shrinkingSqaure (90)
shrinkingSqaure (70)
shrinkingSqaure (50)
shrinkingSqaure (30)
shrinkingSqaure (10)

turtle.done()