import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

lang = 5
times = 10
for i in range (times):
    for z in range (4):
        turtle_instance.forward(lang)
        turtle_instance.right(90)
    lang += 5



turtle.done()
