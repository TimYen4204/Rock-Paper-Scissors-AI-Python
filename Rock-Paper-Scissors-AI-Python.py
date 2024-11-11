#Temporary. Old code that was used for testing turtle graphics.

# Turtle Graphics Travels

# Turtle module imported to be able to use its' functions.
import turtle

# Created cute_turtle object to be used.
cat = turtle.Turtle()

# Set speed for turtle.
cat.speed(5)

# Set fill in color 1st Roadblock.
cat.fillcolor('blue')

# Creates the 1st Vertical Roadblock.
cat.penup()
cat.goto(-150,-200)
cat.pendown()
cat.begin_fill()
cat.left(90)
cat.forward(80)
cat.right(90)
cat.forward(10)
cat.right(90)
cat.goto(-140, -200)
cat.right(90)
cat.forward(10)
cat.end_fill()

# Creates the 2nd Vertical Roadblock.
cat.penup()
cat.goto(-100,-200)
cat.pendown()
cat.begin_fill()
cat.right(90)
cat.forward(130)
cat.right(90)
cat.forward(10)
cat.right(90)
cat.goto(-90,-200)
cat.right(90)
cat.forward(10)
cat.end_fill()

# Creates the 3rd Vertical Roadblock.
cat.penup()
cat.goto(-50,-200)
cat.pendown()
cat.begin_fill()
cat.right(90)
cat.forward(80)
cat.right(90)
cat.forward(10)
cat.right(90)
cat.goto(-40, -200)
cat.right(90)
cat.forward(10)
cat.end_fill()

# Creates the 4th Vertical Roadblock.
cat.penup()
cat.goto(20,-200)
cat.pendown()
cat.begin_fill()
cat.right(90)
cat.forward(100)
cat.right(90)
cat.forward(10)
cat.right(90)
cat.goto(30, -200)
cat.right(90)
cat.forward(10)
cat.end_fill()

# Creates the 5th Vertical Roadblock.
cat.penup()
cat.goto(80,-200)
cat.pendown()
cat.begin_fill()
cat.right(90)
cat.forward(260)
cat.right(90)
cat.forward(10)
cat.right(90)
cat.goto(90, -200)
cat.right(90)
cat.forward(10)
cat.end_fill()

# Creates the 6th Vertical Roadblock.
cat.penup()
cat.goto(140,-200)
cat.pendown()
cat.begin_fill()
cat.right(90)
cat.forward(140)
cat.right(90)
cat.forward(10)
cat.right(90)
cat.goto(150, -200)
cat.right(90)
cat.forward(10)
cat.end_fill()

# Creates the 1st Horizontal Roadblock.
cat.penup()
cat.goto(-100,-60)
cat.pendown()
cat.begin_fill()
cat.right(90)
cat.forward(10)
cat.right(90)
cat.forward(50)
cat.right(90)
cat.forward(10)
cat.goto(-100,-60)
cat.end_fill()

# Creates the 2nd Horizontal Roadblock.
cat.penup()
cat.goto(-50,-110)
cat.pendown()
cat.begin_fill()
cat.right(180)
cat.forward(10)
cat.right(90)
cat.forward(60)
cat.right(90)
cat.forward(10)
cat.right(90)
cat.goto(-50,-110)
cat.end_fill()

# Creates the 3rd Horizontal Roadblock.
cat.penup()
cat.goto(20,-90)
cat.pendown()
cat.begin_fill()
cat.right(90)
cat.forward(10)
cat.right(90)
cat.forward(50)
cat.right(90)
cat.forward(10)
cat.right(90)
cat.goto(20,-90)
cat.end_fill()

# Creates the 4th Horizontal Roadblock.
cat.penup()
cat.goto(80,70)
cat.pendown()
cat.begin_fill()
cat.right(90)
cat.forward(10)
cat.right(90)
cat.forward(60)
cat.right(90)
cat.forward(10)
cat.right(90)
cat.goto(80,70)
cat.end_fill()

# Creates the 5th Horizontal Roadblock.
cat.penup()
cat.goto(140,-50)
cat.pendown()
cat.begin_fill()
cat.right(90)
cat.forward(10)
cat.right(90)
cat.forward(60)
cat.right(90)
cat.forward(10)
cat.right(90)
cat.goto(140,-50)
cat.end_fill()

# Positions the turtle-cat object.
cat.penup() 
cat.goto(-200,-200)
cat.left(90)
cat.pendown()
cat.pensize(2)

# Indicates the movements of the turtle:
# Hori-1
cat.left(90)
cat.forward(40)

# Vert-1
cat.left(90)
cat.forward(85)

# Hori-2
cat.right(90)
cat.forward(55)

# Vert-2
cat.left(90)
cat.forward(50)

# Hori-3
cat.right(90)
cat.forward(45)

# Vert-3
cat.right(90)
cat.forward(50)

# Hori-4
cat.left(90)
cat.forward(75)

# Vert-4
cat.left(90)
cat.forward(20)

# Hori-5
cat.right(90)
cat.forward(60)

# Vert-5
cat.left(90)
cat.forward(160)

# Hori-6
cat.right(90)
cat.forward(60)

# Vert-6
cat.right(90)
cat.forward(120)

# Hori-7
cat.left(90)
cat.forward(65)

# Vert-7
cat.right(90)
cat.goto(200,-200)
