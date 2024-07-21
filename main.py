import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("red")
drawing_board.title("Python Turtle")

angle = 150
pointies = 10
ROTATION = 360/pointies


turtle.color("black","white")

turtle.begin_fill()

for i in range(pointies):


 turtle.forward(100)
 turtle.right(angle)
 turtle.forward(100)
 turtle.left(angle)
 turtle.right(ROTATION)

turtle.end_fill()
turtle.done()