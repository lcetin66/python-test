import turtle

drawing_board = turtle.Screen()
drawing_board.title("Turtle spiral")
drawing_board.bgcolor("black")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
turtle_instance.speed(0)

turtle_colors = ["red", "orange","yellow","white","light blue","blue","green"]
for i in range(50):
    turtle_instance.color(turtle_colors[i % 7])
    turtle_instance.circle(3*i)
    turtle_instance.circle(-3*i)
    turtle_instance.left(i*2)

#turtle.done()
turtle.mainloop()