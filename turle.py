import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

# bes uclu yildiz ici bos
'''for i in range(5):
    turtle_instance.left(72)
    turtle_instance.forward(200)
    turtle_instance.right(144)
    turtle_instance.forward(200)'''

# ic ice gecmis döner kareler
'''for i in range(24):
    turtle_instance.right(15)
    for j in range(4):
        turtle_instance.forward(100)
        turtle_instance.right(90)'''

# 5 basli yildiz pentagram
'''num_sides= 5
angle =360/num_sides*2
side_length = 100

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)'''

# büyüklügü gittikce artan kareler
'''lang = 5
times = 10
artis = 5  # ilk artış miktarı

for i in range(times):
    for z in range(4):
        turtle_instance.forward(lang)
        turtle_instance.right(90)
    lang += artis       # önceki artış miktarı kadar büyüt
    artis += 5          # artış miktarını da 5 artır'''

turtle.done()

